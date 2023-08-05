# 12) Create a function that returns fibonacci sequence with the given number of elements in a tuple. For example: fib(5) should return (0, 1, 1, 2, 3).
def fib(number):
    sequence_list = []
    if number == 1:
        sequence_list = [0]
    else:
        sequence_list = [0, 1]
        for i in range(1, number - 1):
            sequence_list.append(sequence_list[i - 1] + sequence_list[i])
    return tuple(sequence_list)

print(fib(5))