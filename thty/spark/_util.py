from pyspark.sql import (DataFrame, HiveContext)


def store_to_hive(hc: HiveContext, data: DataFrame, odb: str, otbl: str, use_parquet: bool=True) -> None:
    """
    Store the data in `data` to {odb}.{otbl}
    :param hc:
    :param data:
    :param odb:
    :param otbl:
    :return: None
    """
    parquet = ""
    if use_parquet:
        parquet = "stored as parquet"
    data.createOrReplaceTempView("thty_default")
    hc.sql(f"drop table if exists {odb}.{otbl}")
    query = f"create table {odb}.{otbl} {parquet} as select * from thty_default"
    hc.sql(query)


def get_hive_table(hc: HiveContext, idb: str, itbl: str) -> DataFrame:
    """
    Get a dataframe
    :param hc:
    :param idb:
    :param itbl:
    :return: DataFrame
    """
    sdf = hc.table(f"{idb}.{itbl}")
    return sdf