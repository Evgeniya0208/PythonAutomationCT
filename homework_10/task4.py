from functools import reduce
from homework_10.task3 import fruit_price_with_discount


total_price = sum(fruit_price_with_discount.values())
print(total_price)


def calculate_total_price(dict):
    total = reduce(lambda t, v: t + dict[v], dict, 0)
    return total


print(calculate_total_price(fruit_price_with_discount))