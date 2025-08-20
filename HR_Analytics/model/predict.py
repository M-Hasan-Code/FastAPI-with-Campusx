import pickle
import pandas as pd
from fastapi.responses import JSONResponse

with open('model/lr.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'
class_labels = model.classes_.tolist()

def predict_output(user_input: pd.DataFrame):
    probas = model.predict_proba(user_input)[0]
    class_proba_dict = dict(zip(class_labels, probas))
    
    max_index = probas.argmax()
    max_proba = probas[max_index]
    
    # Just return the class with the highest probability
    predict_class = class_labels[max_index]

    return JSONResponse(status_code=200, content={
        'predicted_category': predict_class,
        'max_probability': round(float(max_proba), 4),
        'probabilities': class_proba_dict,
    })