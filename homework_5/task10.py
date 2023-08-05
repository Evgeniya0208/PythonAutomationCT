# 10) Write a function called print_invoice that prints an invoice for a purchase. The function should take a positional
# argument customer_name and two keyword arguments: items (a list of purchased items) and discount. Assume that discount
# has a default value of 0.
def print_invoice(customer_name, items=None, discount=0):
    if items is None:
        items = []
    print(customer_name)
    print(items)
    print(discount)

print_invoice("Jane", items=["book", "table", "chare"], discount=6),