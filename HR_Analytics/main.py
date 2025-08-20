from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION
import pandas as pd

app = FastAPI()

# human readable       
@app.get('/')
def home():
    return {'message':'HR Analytics API'}

# machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        'city_development_index': data.city_development_index,
        'gender': data.gender,
        'relevent_experience': data.relevent_experience,
        'enrolled_university': data.enrolled_university,
        'education_level': data.education_level,
        'major_discipline': data.major_discipline,
        'company_type': data.company_type,
        'last_new_job': data.last_new_job,
        'training_hours': data.training_hours,
        'exp_level': data.exp_level,
        'size_label': data.size_label
    }])

    try:
        prediction = predict_output(input_df)  # ← Pass DataFrame, not class
        return prediction  # Already a JSONResponse
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})