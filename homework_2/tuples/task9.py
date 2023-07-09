#Task 9: Tuple Immutability
#Explain the concept of immutability in Python tuples and provide an example that demonstrates the immutability of tuples.

"""Tuples are a data type that belongs to the sequence data type category.
They're similar to lists in Python, but they have the property of being immutable.
We can't change the elements of a tuple, but we can execute a variety of actions on them such as
count, index, type, etc."""

my_tuple = (1, 2, 3, 4, 5)

"We can't assign new item to tuple"
my_tuple[5] = 6
"We can't delete existing item from tuple"
del my_tuple[0]