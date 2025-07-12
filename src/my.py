def calculate_taxes(prices: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""
    if tax_rate < 0:
        raise ValueError('Неверный налоговый процент')

    taxed_prices = []
    for price in prices:
        if price <= 0:
            raise ValueError('Неверная цена')
        tax = price * tax_rate / 100
        taxed_prices.append(price + tax)

    return taxed_prices


def calculate_tax(price: float, tax_rate: float, *, discount: float = 0) -> float:
    if not isinstance(price, (int, float)):
        raise TypeError("Цена должна быть числом (int или float)")
    if not isinstance(tax_rate, (int, float)):
        raise TypeError("Налоговая ставка должна быть числом (int или float)")
    if not isinstance(discount, (int, float)):
        raise TypeError("Скидка должна быть числом (int или float)")

    if price < 0:
        raise ValueError('Неверная цена')

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Неверный налоговый процент')

    final_price = price + (price * tax_rate / 100)
    final_price_with_discount = final_price - (final_price * discount / 100)
    return round(final_price_with_discount, 2)


