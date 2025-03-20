import pytest

from src.questionnaire.agent import QuestionnarieAgent

@pytest.fixture(name="prompt_example")
def prompt_example_fixture() -> str:
	"""Fixture that contains a prompt to call OpenAI API

	Returns:
		str: The test prompt
	"""
	return """
		This is a prompt to make a unitary test.
		Your task is only to answer "yes" if there is no exception in the API call.
 	"""
  
@pytest.fixture(name="agent_example")
def agent_example_fixture() -> QuestionnarieAgent:
	"""Gives an Agent object to call the inner functions.

	Returns:
		Agent: The Agent that will be used to the tests.
	"""
	return QuestionnarieAgent()