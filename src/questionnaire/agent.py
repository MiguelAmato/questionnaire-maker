import os

from dotenv import load_dotenv

from openai import OpenAI

from questionnaire.schemas import Questionnaire
from questionnaire.prompts import PROMPT

class QuestionnarieAgent:
    """Main logic for the Questionnaire maker."""
    
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def call_llm(
        self,
        text:str,
        response_format:Questionnaire=None,
        model:str="gpt-4o-mini",
        temperature:float=0.3,
    ) -> str:
        """Calls the OpenAI API to make a questionnaire about a text.

        Args:
            text (str): The text that you want to make a questionnaire.
            response_format (Questionnaire): questinonaire schema for the response.
            model (str, optional): Set the model from the OpenAI models availables. Defaults to "gpt-4o-mini".
            temperature (float, optional): Set the temperature model. Defaults to 0.3.

        Returns:
            str: Returns de questionnarie. 
        """
        
        messages=[
            {"role": "system", "content": PROMPT.format(text=text)}
        ]
        
        if response_format:
            response = self.client.beta.chat.completions.parse(
                model=model,
                messages=messages,
                response_format=response_format,
            )
        else:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
            )
        
        return (
            response.choices[0].message.parsed
            if response_format
            else response.choices[0].message.content
        ) 