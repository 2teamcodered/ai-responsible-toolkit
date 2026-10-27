REQUIRED={"intended_use","limitations","evaluation","oversight"}
def validate_model_card(card: dict) -> dict:
    missing=sorted(REQUIRED-set(card))
    return {"valid":not missing,"missing":missing}
def risk_item(hazard, likelihood, impact, mitigation):
    return {"hazard":hazard,"likelihood":likelihood,"impact":impact,"mitigation":mitigation,"owner":"assign before launch"}
