from joblib import load

def return_model():
    data_model = load('company_bankcruptcy_prediction.joblib')
    return data_model

