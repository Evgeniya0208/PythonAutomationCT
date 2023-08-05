# Create a function called calculate_total_cost that calculates and returns the total cost of a purchase. The function
# should take one positional argument base_price and two keyword arguments: tax_rate and discount. Assume that tax_rate
# has a default value of 0 and discount has a default value of 0.
def calculate_total_cost(base_price, tax_rate=0, discount=0):
    return base_price + base_price * tax_rate / 100 - base_price * discount / 100


print(calculate_total_cost(120, 18, 7))
