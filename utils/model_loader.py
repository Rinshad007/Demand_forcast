import joblib

model = joblib.load("RandomForest.pkl")
columns = joblib.load("rf_model_columns.pkl")

def load_model():
    return model, columns