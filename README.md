#  About
Example large-scale model.  

## Command-line software (CLI) called `THTY`

    score_dense(idb:str, itbl:str, odb:str, otbl:str, prediction:str='prediction') -> None
        Score the model on a dense version of the large featureset
        :param idb: Inbound database
        :param itbl: Inbound table (eg large featureset)
        :param odb: Outbound database
        :param otbl: Outbound table
        :param prediction: Name of the column that is the prediction
        :return: None

    score_sparse(idb:str, itbl:str, odb:str, otbl:str, prediction:str='prediction') -> None
        Score the model on a sparse version of the large featureset
        :param idb: Inbound database
        :param itbl: Inbound table (eg large featureset)
        :param odb: Outbound database
        :param otbl: Outbound table
        :param prediction: Name of the column that is the prediction
        :return: None
### Example usage
```bash
THTY score_dense idb=hcaadvaph_wk_playground itbl=ad09492_temporary odb=hcaadvaph_wk_playground otbl=ad09492_temporary_out prediction=yhat

THTY score_sparse idb=hcaadvaph_wk_playground itbl=ad09492_temporary odb=hcaadvaph_wk_playground otbl=ad09492_temporary_out prediction=yhat

```

## Python package `thty`

###  What methods are exposed:
    score_dense(idb:str, itbl:str, odb:str, otbl:str, prediction:str='prediction') -> None
        Score the model on a dense version of the large featureset
        :param idb: Inbound database
        :param itbl: Inbound table (eg large featureset)
        :param odb: Outbound database
        :param otbl: Outbound table
        :param prediction: Name of the column that is the prediction
        :return: None

    score_sparse(idb:str, itbl:str, odb:str, otbl:str, prediction:str='prediction') -> None
        Score the model on a sparse version of the large featureset
        :param idb: Inbound database
        :param itbl: Inbound table (eg large featureset)
        :param odb: Outbound database
        :param otbl: Outbound table
        :param prediction: Name of the column that is the prediction
        :return: None

    spark_score_dense(hc:pyspark.sql.session.SparkSession, data:pyspark.sql.dataframe.DataFrame, prediction:str) -> pyspark.sql.dataframe.DataFrame
        Score the Spark DataFrame
        :param hc: SparkSession
        :param data: Spark dataframe
        :param prediction: label for the prediction
        :return: Spark dataframe with the identifier and prediction

    spark_score_sparse(hc:pyspark.sql.session.SparkSession, data:pyspark.sql.dataframe.DataFrame, prediction:str) -> pyspark.sql.dataframe.DataFrame
        Score the Spark DataFrame
        :param hc: SparkSession
        :param data: Spark dataframe
        :param prediction: label for the prediction
        :return: Spark dataframe with the identifier and prediction

### Example usage

```python
from thty import spark_score_dense
o = spark_score_dense(hc, data, prediction='prediction')
o.show(3)
+------+--------------------+
|  id|          prediction|
+------+--------------------+
| 86087|  0.3671088222227899|
| 97077|0.001998061647463...|
|163017|1.600337345181496E-4|
+------+--------------------+
```

