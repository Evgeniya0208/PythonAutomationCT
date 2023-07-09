# Task 9: Set FrozenSet
# Explain the concept of a frozen set in Python and discuss its characteristics and use cases.

"""Frozenset is an immutable version of a Python set object.
Frozensets could be used as a dictionary key or as an element from another set.
"""
food = {"Bread", "Eggs", "Banana"}
fridge = frozenset(food)
print(fridge)

car = {"Brand": "Fiat", "Fuel Type": "Petrol", "Body Type": "Hatchback", "Color": "Read"}
key = frozenset(car)
print(key)