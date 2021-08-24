import re

from pyspark.sql import (DataFrame, SparkSession)
from pyspark.sql import functions as F
import numpy as np

from tiramisu import lil_to_csr
from thty._const import (IDENTIFIER, GMAD_NUMERIC_FEATURE_SIZE)
from thty._model import Model


def spark_score_dense(hc: SparkSession, data: DataFrame, prediction: str) -> DataFrame:
    """
    Score the Spark DataFrame
    :param hc: SparkSession
    :param data: Spark dataframe
    :param prediction: label for the prediction
    :return: Spark dataframe with the identifier and prediction
    """
    selected_indices = Model.get_numeric_feature_indices()
    all_cols = ['mcid']
    numeric_columns = np.array([c for c in data.columns if not re.match('^(mcid)|(cat.*)', c)])
    numeric_columns = numeric_columns[selected_indices.feature_index.values]
    all_cols.extend(list(numeric_columns))

    bc_columns = hc.sparkContext.broadcast(numeric_columns)

    @F.pandas_udf("mcid long, pid integer, yhat double", F.PandasUDFType.GROUPED_MAP)
    def _score(pdf):
        cols = bc_columns.value
        x = pdf[cols].values
        x = np.nan_to_num(x)
        odf = pdf[['mcid', 'pid']].copy()
        pred = Model.predict(x)
        odf['yhat'] = [e.item() for e in np.nan_to_num(pred)]
        return odf

    sdf = data.select(*[data[c] for c in all_cols])\
        .withColumn("pid", F.spark_partition_id())\
        .groupBy("pid")\
        .apply(_score)\
        .selectExpr("mcid", f"yhat as {prediction}")
    return sdf


def spark_score_sparse(hc: SparkSession, data: DataFrame, prediction: str) -> DataFrame:
    """
    Score the Spark DataFrame
    :param hc: SparkSession
    :param data: Spark dataframe
    :param prediction: label for the prediction
    :return: Spark dataframe with the identifier and prediction
    """
    @F.pandas_udf("mcid long, pid integer, yhat double", F.PandasUDFType.GROUPED_MAP)
    def _score(pdf):
        x = lil_to_csr(pdf.colptr.values, pdf.val.values, shape=(pdf.shape[0], GMAD_NUMERIC_FEATURE_SIZE))
        x.eliminate_zeros()
        odf = pdf[['mcid', 'pid']].copy()
        pred = Model.sel_predict(x)
        odf['yhat'] = [e.item() for e in np.nan_to_num(pred)]
        return odf

    sdf = data.select("mcid", "colptr", "val")\
        .withColumn("pid", F.spark_partition_id())\
        .groupBy("pid")\
        .apply(_score)\
        .selectExpr("mcid", f"yhat as {prediction}")
    return sdf
