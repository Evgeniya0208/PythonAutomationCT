# Task 6: Dictionary Sorting
# Given the dictionary my_dict = {"b": 2, "c": 1, "a": 3}, print the dictionary after sorting it based on the keys in ascending order.
my_dict = {"b": 2, "c": 1, "a": 3}

sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)