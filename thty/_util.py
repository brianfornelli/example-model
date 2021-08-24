import os.path as osp
from datetime import datetime
from types import SimpleNamespace
from bidarka import read_settings


def script_path(key, *keys):
    return osp.join(osp.dirname(__file__), key, *keys)


def current_scoredate() -> str:
    run_date = datetime.today().strftime('%Y-%m-%d')
    return str(run_date)


def load_config(key: str) -> SimpleNamespace:
    settings = read_settings(key=key)
    return SimpleNamespace(**settings)
