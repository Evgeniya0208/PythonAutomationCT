# Task 1: File Reading
# Write a Python program that reads the contents of a text file named "hw_data.txt" and prints them to the console.
with open('hw_data.txt') as reader:
    print(reader.read())