import os.path as osp
import os

from pyspark.sql import SparkSession
from bidarka import read_settings


ENV_VARIABLES = read_settings('ENV_VARIABLES')
APP_NAME = read_settings('APP_NAME')
VENV_PATH = read_settings('VENV_PATH')
SPARK_CONFIG = read_settings('SPARK_CONFIG')


def _setup_environment_variables() -> None:
    if ENV_VARIABLES is not None and isinstance(ENV_VARIABLES, dict):
        for k, v in ENV_VARIABLES.items():
            os.environ[k] = v


def get_spark_session() -> SparkSession:
    _setup_environment_variables()
    warehouse_location = osp.abspath('spark-warehouse')

    SparkSession.builder.appName(APP_NAME)
    SparkSession.builder.config("spark.sql.warehouse.dir", warehouse_location)
    for k, v in SPARK_CONFIG:
        SparkSession.builder.config(k, v)
    SparkSession.builder.config("spark.yarn.appMasterEnv.PYSPARK_PYTHON", "./pyenv/bin/python")
    SparkSession.builder.config("spark.yarn.dist.archives", f"{VENV_PATH}#pyenv")
    SparkSession.builder.enableHiveSupport()
    context = SparkSession.builder.getOrCreate()
    return context
