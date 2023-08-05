# 6) Implement a function called calculate_shipping_cost that calculates and returns the shipping cost for an item.
# The function should take two positional arguments: item_price and weight, and one keyword argument discount.
# Assume that discount has a default value of 0.
def calculate_shipping_cost(item_price, weight, discount=0):
    full_cost = item_price * weight
    discount_sum = full_cost * discount / 100
    return full_cost - discount_sum


print(calculate_shipping_cost(10, 200, discount=10))
