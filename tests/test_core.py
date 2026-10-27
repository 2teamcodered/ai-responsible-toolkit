from responsible_ai.core import validate_model_card
def test_card_validation(): assert validate_model_card({})["valid"] is False
