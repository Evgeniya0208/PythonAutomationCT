# Task: Number Sum
# Write a Python program that takes an integer as input from the user and calculates the sum of all numbers from 1 to that integer (inclusive). Display the result. Use a loop and conditional statements to implement this.
number = int(input("Please enter a number:   "))

i = 0
sum_of_all_numbers = 0

while i <= number:
    sum_of_all_numbers += i
    i += 1
else: print(sum_of_all_numbers)

