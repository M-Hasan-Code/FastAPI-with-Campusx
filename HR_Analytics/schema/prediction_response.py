
from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category: str = Field(
        ...,
        description="The predicted insurance premium category",
        example="0.0"
    )
    confidence: float = Field(
        ...,
        description="Model's confidence score for the predicted class (range: 0 to 1)",
        example=0.8432
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Probability distribution across all possible classes",
        example={"0.0": 0.07, "0.1": 0.93}
    )