# Task: Multiplication Table
# Write a Python program that takes an integer as input from the user and prints the multiplication table for that number from 1 to 10. Display the result in the format: "Number x Multiplier = Result". Use loops and conditional statements to implement this.
number = int(input("Please enter a number:   "))

for i in range(1, 11):
    print(number, " * ", i, " = ", number*i)
