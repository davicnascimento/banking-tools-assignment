from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "banking_products.xlsx"


def search_banking_products(query: str) -> list[dict]:
    """TODO: pesquisar produtos no ficheiro Excel e devolver os resultados."""
    raise NotImplementedError("Implementar a pesquisa no Excel")
