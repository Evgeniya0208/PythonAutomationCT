#Task 6: Given a list [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45].
# You need to sort it in ascending order using any sorting algorithm. Do not user built-in "sort" or "sorted" method.

list_for_sorting_1 = [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]
sorted_list = []

while list_for_sorting_1:
    minimum = list_for_sorting_1[0]
    for x in list_for_sorting_1:
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)
    list_for_sorting_1.remove(minimum)

print(sorted_list)


list_for_sorting_2 = [13, 59, 56, 13, 84, 58, 43, 4, 74, 8, 32, 100, 92, 50, 29, 24, 61, 39, 99, 45]

for i in range(len(list_for_sorting_2)):
    for j in range(i + 1, len(list_for_sorting_2)):
        if list_for_sorting_2[i] > list_for_sorting_2[j]:
            list_for_sorting_2[i], list_for_sorting_2[j] = list_for_sorting_2[j], list_for_sorting_2[i]

print(list_for_sorting_2)