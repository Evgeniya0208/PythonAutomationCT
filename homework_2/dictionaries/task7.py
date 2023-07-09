# Task 7: Dictionary Merging
# Given two dictionaries dict1 = {"a": 1, "b": 2} and dict2 = {"c": 3, "d": 4}, merge them into a single dictionary named merged_dict.
# Print the merged dictionary.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)