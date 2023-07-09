# Task 6: File Word Count
# Write a Python program that reads a text file named "hw_data.txt" and counts the number of words in the file. Print the word count.
with open('hw_data.txt') as reader:
    data = reader.read()
    lines = data.split()
print(len(lines))
