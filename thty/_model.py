from typing import Union

import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
import joblib

from thty._const import (MODEL_PATH, ISOREG_PATH, FEATURE_PATH)


class Model:
    @staticmethod
    def get_numeric_feature_indices() -> np.array:
        return pd.read_csv(FEATURE_PATH)

    @staticmethod
    def predict(x: Union[csr_matrix, np.array]) -> np.array:
        model = joblib.load(MODEL_PATH)
        iso_reg = joblib.load(ISOREG_PATH)
        predictions = model.predict_proba(x)[:, 1]
        return np.nan_to_num(iso_reg.predict(predictions))

    @staticmethod
    def sel_predict(x: Union[csr_matrix, np.array]) -> np.array:
        feature_indices = pd.read_csv(FEATURE_PATH)
        model = joblib.load(MODEL_PATH)
        iso_reg = joblib.load(ISOREG_PATH)
        x_data = x[:, feature_indices.feature_index.values]
        predictions = model.predict_proba(x_data)[:, 1]
        return np.nan_to_num(iso_reg.predict(predictions))
