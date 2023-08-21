fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Banana", "Apple"]

def filter_duplicate_fruits(list_of_fruits):
   return list(filter(lambda x: list_of_fruits.count(x) == 1, list_of_fruits))

print(filter_duplicate_fruits(fruits))