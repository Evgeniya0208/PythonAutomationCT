#Task 2: Set Operations
#Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, perform the following set operations and print the results:
#Union: Combine the elements from both sets without duplicates.
#Intersection: Find the common elements between the two sets.
#Difference: Find the elements that are in set1 but not in set2.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1 | set2

print(set3)
print(set1.intersection(set2))
print(set1.difference(set2))