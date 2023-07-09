# Task 8: File Line Reversal
# Write a Python program that reads the contents of a text file named "hw_data.txt" and writes the lines in reverse order to a new text file named "reversed.txt".
with open("hw_data.txt", 'r') as source, open("reversed.txt", 'w') as reversed:
    data = source.read()
    reversed_data = data[::-1]
    reversed.write(reversed_data)
