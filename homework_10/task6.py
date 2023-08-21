from homework_10.task1 import Fruit


def is_fruit_available(fruit):
    values = [item.value for item in Fruit]
    return fruit in values

print(is_fruit_available("Apple"))
print(is_fruit_available("Banana"))
print(is_fruit_available("banana"))