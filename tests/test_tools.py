from src.tools import get_customer_card_info


def test_card_lookup_is_callable():
    assert callable(get_customer_card_info)
