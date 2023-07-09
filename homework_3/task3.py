# Task 3: File Appending
# Write a Python program that prompts the user to enter a line of text and appends it to an existing text file named "hw_data.txt".
lines = [" ", input("Please enter some line of text!!   "), input("Please enter one more line of text!!   ")]
with open('hw_data.txt', 'a') as f:
    f.writelines('\n'.join(lines))
