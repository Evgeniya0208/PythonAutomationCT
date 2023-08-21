from homework_10.task1 import Fruit

fruit_price = {}
fruit_price[Fruit.GRAPE.value] = 42
fruit_price[Fruit.APPLE.value] = 18
fruit_price[Fruit.BANANA.value] = 24
fruit_price[Fruit.ORANGE.value] = 35
fruit_price[Fruit.STRAWBERRY.value] = 50

print(fruit_price)


def apply_discount(fruit_dict: dict):
    updated_dict = dict(
        zip(
            fruit_dict,
            map(
                lambda x: x - (x * 0.1),
                fruit_dict.values()
            )
        )
    )
    return updated_dict


fruit_price_with_discount = apply_discount(fruit_price)
print(fruit_price_with_discount)
