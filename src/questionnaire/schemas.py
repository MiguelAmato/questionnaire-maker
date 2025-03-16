from typing import List
from pydantic import BaseModel

class Options(BaseModel):
    """Schema for the options."""
    
    option: str

class Question(BaseModel):
    """Schema for the questions."""
    
    question: str
    options: List[Options]
    

class Questionnaire(BaseModel):
    """Schema for the response format."""
    
    questions: List[Question]

    