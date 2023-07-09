# Task 6: Set Intersection Update
# Given two sets set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}, use the appropriate set method to update set1
# with the elements that are common between set1 and set2. Print the updated set1.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

set1.intersection_update(set2)
print(set1)