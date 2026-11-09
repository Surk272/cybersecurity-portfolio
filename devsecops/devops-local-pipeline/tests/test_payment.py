import pytest

from app.payment import calculate_total


def test_calculate_total():
    assert calculate_total(100, 0.19) == 119.0


def test_zero_amount():
    assert calculate_total(0, 0.19) == 0.0


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_total(-100, 0.19)


def test_invalid_tax_rate():
    with pytest.raises(ValueError):
        calculate_total(100, 1.5)