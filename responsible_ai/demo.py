from .core import validate_model_card
print(validate_model_card({"intended_use":"demo","limitations":"none","evaluation":"manual","oversight":"human"}))
