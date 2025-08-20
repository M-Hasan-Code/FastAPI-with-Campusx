from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

app = FastAPI()

class UserInput(BaseModel):
    city_development_index: Annotated[float, Field(..., description='City development index of the user', examples=[0.8233])]
    gender: Annotated[Literal['Male', 'Female'], Field(...)]
    relevent_experience: Annotated[Literal['Has relevent experience', 'No relevent experience'], Field(...)]
    enrolled_university: Annotated[Literal['no_enrollment', 'Full time course', 'Part time course'], Field(...)]
    education_level: Annotated[Literal['Graduate', 'Masters', 'High School', 'Phd', 'Primary School'], Field(...)]
    major_discipline: Annotated[Literal['STEM', 'Business Degree', 'Arts', 'Humanities', 'No Major', 'Other'], Field(...)]
    experience: Annotated[int, Field(...)]
    company_size: Annotated[Literal['50-99', '<10', '10000+', '5000-9999', '1000-4999', '10/49', '100-500', '500-999'], Field(...)]
    company_type: Annotated[Literal['Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other', 'Public Sector', 'NGO'], Field(...)]
    last_new_job: Annotated[int, Field(...)]
    training_hours: Annotated[int, Field(...)]

    @computed_field
    @property
    def exp_level(self) -> str:
        if self.experience <= 5:
            return 'small_exp'
        elif self.experience <= 10:
            return 'medium_exp'
        elif self.experience <= 15:
            return 'high_exp'
        else:
            return 'very_high_exp'

    @computed_field
    @property
    def size_label(self) -> str:
        if self.company_size == '<10':
            return 'micro'
        elif self.company_size in ['10/49', '50-99']:
            return 'small'
        elif self.company_size in ['100-500', '500-999']:
            return 'medium'
        elif self.company_size in ['1000-4999', '5000-9999']:
            return 'large'
        elif self.company_size == '10000+':
            return 'enterprise'
        else:
            return 'unknown'