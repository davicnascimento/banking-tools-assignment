from src.config import Settings
from src.prompt import SYSTEM_PROMPT
from src.tools import search_banking_products

TOOLS = [{
    "type": "function",
    "function": {
        "name": "search_banking_products",
        "description": "Pesquisa produtos bancários no catálogo Excel.",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string", "description": "Termos a pesquisar no catálogo"}},
            "required": ["query"],
        },
    },
}]


def answer_question(settings: Settings, question: str) -> str:
    """TODO: implementar o ciclo completo de tool calling com o Groq."""
    raise NotImplementedError("Implementar o agente com tool calling")
