import os
import json
from dotenv import load_dotenv
from questionnaire.agent import QuestionnarieAgent
from questionnaire.schemas import Questionnaire

load_dotenv()

DATA_PATH = os.getenv("DATA_PATH")


def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("¡Bienvenido al creador de cuestionarios!\n\n")
    text = input("Escribe aquí el texto al que se le hará un cuestionario: ")
    questionnarie = QuestionnarieAgent()
    response = questionnarie.call_llm(text=text, response_format=Questionnaire)
    print("\n\n")
    print(json.dumps(response.dict(), indent=4, ensure_ascii=False))
    path = os.path.join(DATA_PATH, "result.json")
    with open(path, "w") as file:
        json.dump(response.model_dump(), file, indent=4)
    print("JSON succesfully saved!")


if __name__ == "__main__":
    main()