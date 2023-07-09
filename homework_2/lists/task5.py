#Task 5: Using list comprehension create a list that contains numbers from 10 to 1 in descending order.
my_list = [x for x in range(1, 11)]
my_list.sort(reverse=True)
print(my_list)