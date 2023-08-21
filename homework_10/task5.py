from homework_10.task3 import fruit_price_with_discount


def check_fruit_conditions(dict, str):
    has_a = any("a" in key for key in dict)
    print(has_a)
    has_all = all(key.startswith(str) for key in dict)
    print(has_all)

check_fruit_conditions(fruit_price_with_discount, "A")
check_fruit_conditions(fruit_price_with_discount, "a")


fruits = ["Apple"]
check_fruit_conditions(fruits, "A")
check_fruit_conditions(fruits, "a")