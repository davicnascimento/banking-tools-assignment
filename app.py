from src.agent import answer_question
from src.config import load_settings


def main() -> None:
    question = input("Pergunta: ").strip()
    if not question:
        print("Escreva uma pergunta para continuar.")
        return
    try:
        print(answer_question(load_settings(), question))
    except Exception as error:
        print(f"Erro ao processar a pergunta: {error}")


if __name__ == "__main__":
    main()
