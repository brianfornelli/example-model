from ._util import script_path

PREDICTION = 'prediction'
RESOURCES = 'resources'
GMAD_NUMERIC_FEATURE_SIZE = 16990
IDENTIFIER = 'mcid'

MODEL_PATH = script_path(RESOURCES, 'model', 'LightGbmClassifier.pkl')
ISOREG_PATH = script_path(RESOURCES, 'model', 'IsotonicReg.pkl')
FEATURE_PATH = script_path(RESOURCES, 'model', 'feature_indices.csv')
