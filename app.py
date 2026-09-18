from src.agent import answer_question
from src.config import load_settings


def main() -> None:
    try:
        settings = load_settings()
    except Exception as error:
        print(f"Erro ao carregar a configuração: {error}")
        return

    print("Escreva 'exit' ou 'quit' para sair.")

    while True:
        try:
            question = input("Pergunta: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nAté breve.")
            return

        if question.lower() in {"exit", "quit"}:
            print("Até breve.")
            return

        if not question:
            print("Escreva uma pergunta para continuar.")
            continue

        try:
            print(answer_question(settings, question))
        except Exception as error:
            print(f"Erro ao processar a pergunta: {error}")


if __name__ == "__main__":
    main()
