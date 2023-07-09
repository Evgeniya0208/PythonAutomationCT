#Task 5: Set Addition and Removal
# Given an empty set my_set, perform the following operations and print the resulting set after each step:
#
# Add the element "apple" to the set.
# Add the elements "banana" and "cherry" to the set.
# Remove the element "apple" from the set.

my_set = set()
my_set.add("apple")
print(my_set)

my_list = ["banana", "cherry"]
my_set.update(my_list)
print(my_set)

my_set.remove("apple")
print(my_set)