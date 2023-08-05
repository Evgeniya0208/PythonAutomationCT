# 3) Implement a function called calculate_expenses that calculates and returns the total expenses for a trip. The function should take one positional argument hotel_cost, and two keyword arguments: food_cost and transportation_cost.
# Assume that food_cost and transportation_cost have default values of 0.
def calculate_expenses(hotel_cost, food_cost=0, transportation_cost=0):
    return hotel_cost + food_cost + transportation_cost


print(calculate_expenses(200, food_cost=50, transportation_cost=120))
