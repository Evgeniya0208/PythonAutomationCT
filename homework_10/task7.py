from homework_10.task1 import Fruit
from homework_10.task3 import apply_discount
from homework_10.task4 import calculate_total_price


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, Fruit, price):
        self.items[Fruit.value] = price

    def calculate_sum_with_discount(self):
        self.items = apply_discount(self.items)
        sum_with_discount = calculate_total_price(self.items)
        return print(f'Total sum is: {sum_with_discount}')


my_cart = ShoppingCart()
my_cart.add_item(Fruit.APPLE, 90)
my_cart.add_item(Fruit.GRAPE, 45)
my_cart.calculate_sum_with_discount()