import pytest

from src.my import calculate_tax


@pytest.mark.parametrize('price, tax_rate, final_price', [(100.0,2.0,102.0),(100.0,10.0,110.0),(50.0,5.0,52.5)])
def test_calculate_tax_normal(price, tax_rate, final_price):
    assert calculate_tax(price, tax_rate) == final_price

@pytest.mark.parametrize('price, tax_rate, final_price, error_msg', [(-100.0,2.0,102.0, 'Неверная цена'),
                                                          (100.0,-10.0,110.0, 'Неверный налоговый процент'),
                                                          (50.0,50000.0,52.5, 'Неверный налоговый процент'),
                                                          (-50.0,-50.0,52.5, 'Неверная цена')])
def test_calculate_tax_ex(price, tax_rate, final_price,error_msg):
    with pytest.raises(ValueError) as exc_info:
        calculate_tax(price, tax_rate)
    assert str(exc_info.value) == error_msg
