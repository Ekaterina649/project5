import pytest
from src.my import calculate_taxes

@pytest.fixture()
def calculate_taxes_values():
    return [200.0, 300.0, 400.0]

# Параметризованный тест для основных случаев
@pytest.mark.parametrize("prices, tax_rate, expected", [
    ([200.0, 300.0, 400.0], 10.0, [220.0, 330.0, 440.0]),
    ([100.0], 0.0, [100.0]),  # нулевая ставка
    ([50.0, 75.0], 20.0, [60.0, 90.0]),  # высокая ставка
    ([], 15.0, []),  # пустой список
])
def test_calculate_taxes(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected

# Параметризованный тест для дробных ставок
@pytest.mark.parametrize("prices, tax_rate, expected", [
    ([200.0, 300.0, 400.0], 7.5, [215.0, 322.5, 430.0]),
    ([100.0], 12.5, [112.5]),
])
def test_calculate_taxes_fractional_rates(prices, tax_rate, expected):
    assert calculate_taxes(prices, tax_rate) == expected

# Параметризованный тест для ошибочных случаев
@pytest.mark.parametrize("prices, tax_rate, expected_error, error_msg", [
    ([100.0], -5.0, ValueError, "Неверный налоговый процент"),  # отрицательная ставка
    ([-1.0, 100.0], 10.0, ValueError, "Неверная цена"),  # отрицательная цена
    ([0.0], 10.0, ValueError, "Неверная цена"),  # нулевая цена
])
def test_calculate_taxes_errors(prices, tax_rate, expected_error, error_msg):
    with pytest.raises(expected_error) as exc_info:
        calculate_taxes(prices, tax_rate)
    assert str(exc_info.value) == error_msg