# Task 7: File Searching
# Write a Python program that prompts the user to enter a search term and searches for occurrences of that term in a text file named "hw_data.txt". Print the line numbers where the search term is found.
word = input("Please enter word for search:   ")
with open('hw_data.txt') as reader:
    lines = reader.readlines()
    for line in lines:
        if line.find(word) != -1:
            print(lines.index(line))
