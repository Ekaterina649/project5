import pytest
from src.my import calculate_taxes

@pytest.fixture()
def calculate_taxes_values():
    return [200.0, 300.0, 400.0]

def test_calculate_taxes(calculate_taxes_values):
    assert calculate_taxes(calculate_taxes_values,10.0) == [220.0, 330.0, 440.0]

def test_calculate_taxes_with_negative_tax_rate(calculate_taxes_values):
    with pytest.raises(ValueError) as ex_fanction:
        calculate_taxes(calculate_taxes_values, -4)
        assert str(ex_fanction) == 'Неверный налоговый процент'

def test_calculate_taxes_with_negative_prices():
    with pytest.raises(ValueError) as ex_function_2:
        calculate_taxes([0.0, -5,0], 10.0)
        assert str(ex_function_2) == 'Неверная цена'