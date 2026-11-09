def calculate_total(amount: float, tax_rate: float) -> float:
    if amount < 0:
        raise ValueError("Amount cannot be negative")

    if not 0 <= tax_rate <= 1:
        raise ValueError("Invalid tax rate")

    return round(amount * (1 + tax_rate), 2)

