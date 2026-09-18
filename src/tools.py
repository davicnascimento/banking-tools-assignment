from pathlib import Path

import pandas as pd

DATA_FILE = Path(__file__).parent.parent / "data" / "customer_cards.xlsx"
REQUIRED_COLUMNS = {
    "nif",
    "card_id",
    "card_type",
    "last_four_digits",
    "status",
    "pin",
    "expiry_date",
}


def get_customer_card_info(nif: str) -> list[dict]:
    """Devolve os cartões associados a um NIF simulado."""
    if not nif or not nif.strip():
        return []
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Ficheiro de dados não encontrado: {DATA_FILE}")

    frame = pd.read_excel(DATA_FILE, dtype=str).fillna("")
    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"Colunas em falta no Excel: {', '.join(sorted(missing))}")

    customer_nif = nif.strip()
    matches = frame[frame["nif"].str.strip() == customer_nif]
    return matches.to_dict(orient="records")
