# Task 10: Dictionary Conversion
# Given a list of tuples my_list = [("a", 1), ("b", 2), ("c", 3)], convert it into a dictionary named my_dict. Print the resulting dictionary.
my_list = [("a", 1), ("b", 2), ("c", 3)]

my_dict = dict()
for letter, number in my_list:
    my_dict.setdefault(letter, []).append(number)

print(my_dict)