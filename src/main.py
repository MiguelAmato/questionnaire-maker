import os
import json
from questionnaire.agent import QuestionnarieAgent
from questionnaire.schemas import Questionnaire

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("¡Bienvenido al creador de cuestionarios!\n\n")
    text = input("Escribe aquí el texto al que se le hará un cuestionario: ")
    questionnarie = QuestionnarieAgent()
    response = questionnarie.call_llm(text=text, response_format=Questionnaire)
    print("\n\n")
    print(json.dumps(response.dict(), indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()