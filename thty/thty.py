from ._const import PREDICTION
from ._spark import get_spark_session
from .spark import (spark_score_dense, spark_score_sparse, store_to_hive, get_hive_table)


def score_sparse(idb: str, itbl: str, odb: str, otbl: str, prediction: str=PREDICTION) -> None:
    """
    Score the model on a sparse version of the GMAD
    :param idb: Inbound database
    :param itbl: Inbound table (eg GMAD)
    :param odb: Outbound database
    :param otbl: Outbound table
    :param prediction: Name of the column that is the prediction
    :return: None
    """
    _score(idb=idb, itbl=itbl, odb=odb, otbl=otbl, sparse=True, prediction=prediction)


def score_dense(idb: str, itbl: str, odb: str, otbl: str, prediction: str=PREDICTION) -> None:
    """
    Score the model on a dense version of the GMAD
    :param idb: Inbound database
    :param itbl: Inbound table (eg GMAD)
    :param odb: Outbound database
    :param otbl: Outbound table
    :param prediction: Name of the column that is the prediction
    :return: None
    """
    _score(idb=idb, itbl=itbl, odb=odb, otbl=otbl, sparse=False, prediction=prediction)


def _score(idb: str, itbl: str, odb: str, otbl: str, sparse: bool, prediction: str=PREDICTION) -> None:
    hc = get_spark_session()
    sdf = get_hive_table(hc=hc, idb=idb, itbl=itbl)
    if sparse:
        df = spark_score_sparse(hc=hc, data=sdf, prediction=prediction)
    else:
        df = spark_score_dense(hc=hc, data=sdf, prediction=prediction)
    store_to_hive(hc=hc, data=df, odb=odb, otbl=otbl)
