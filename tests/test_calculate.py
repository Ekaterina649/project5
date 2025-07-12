import pytest

from src.my import calculate_tax


@pytest.mark.parametrize('price, tax_rate, discount, final_price', [
        (100.0, 2.0, 0,    102.0),
        (100.0, 10.0, 0,   110.0),
        (50.0,  5.0, 0,    52.5),
        (200,   5,   10,   189.0),   # пример с целыми числами и скидкой
    ])
def test_calculate_tax_normal(price, tax_rate, discount, final_price):
    assert calculate_tax(price, tax_rate, discount=discount) == final_price



@pytest.mark.parametrize('price, tax_rate, discount, error_msg', [
        (-100.0,  2.0, 0, 'Неверная цена'),
        (100.0, -10.0, 0, 'Неверный налоговый процент'),
        (50.0, 50000.0, 0, 'Неверный налоговый процент'),
        (-50.0, -50.0, 0, 'Неверная цена'),
    ])
def test_calculate_tax_ex(price, tax_rate, discount,error_msg):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, tax_rate)
    assert str(exc_info.value) == error_msg


@pytest.mark.parametrize(
    'price, tax_rate, discount',
    [
        ('100', 2.0, 0),
        (100.0, '2', 0),
        (100.0, 2.0, '5'),
    ]
)
def test_calculate_tax_type_error(price, tax_rate, discount):
    with pytest.raises(TypeError):
        calculate_tax(price, tax_rate, discount=discount)


def test_calculate_tax_discount_positional():
    with pytest.raises(TypeError):
        calculate_tax(100, 10, 5)