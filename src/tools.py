from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).parent.parent / "data" / "customer_cards.xlsx"


def get_customer_card_info(nif: str) -> list[dict]:
    """TODO: devolver os cartões associados ao NIF simulado."""
    raise NotImplementedError("Implementar a consulta de cartões no Excel")
