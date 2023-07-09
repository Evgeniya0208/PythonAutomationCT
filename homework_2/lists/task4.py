#Task 4: Given a list with duplicates [1, 2, 3, 4, 3, 1, 5, 2, 6].
# You need to create a new list with all the duplicate elements removed.
# The order of the elements should be preserved. For example, if the input list is [1, 2, 2, 3, 4, 1, 5],
# result will be [1, 2, 3, 4, 5].
list_with_duplicates = [1, 2, 3, 4, 3, 1, 5, 2, 6]
list_with_uhique_values = [*set(list_with_duplicates)]
print(list_with_duplicates)
print(list_with_uhique_values)