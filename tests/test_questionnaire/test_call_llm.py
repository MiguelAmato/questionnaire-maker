import pytest
from src.questionnaire.agent import QuestionnarieAgent

@pytest.mark.asyncio
async def test_call_llm(prompt_example: str, agent_example: QuestionnarieAgent) -> None:
	"""Test the OpenAI API call with the function call_llm.

	Args:
		prompt_example (str): A prompt that will pass to the call_llm.
		agent_example (Agent): An Agent that will use the calls to the inner functions.
	"""
	agent = agent_example
 
	response =  agent.call_llm(text=prompt_example, response_format=None)
 
	assert type(response) == type("Yes")