# Task 5: File Line Count
# Write a Python program that reads a text file named "hw_data.txt" and counts the number of lines in the file. Print the line count.
with open('hw_data.txt') as reader:
    for count, line in enumerate(reader):
        pass

print("Total lines: ", count + 1)