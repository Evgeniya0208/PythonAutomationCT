# Task: Palindrome Checker
# Write a Python program that takes a string as input from the user and checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. Display a message indicating whether the string is a palindrome or not. Use loops and conditional statements to implement this.
line = input("Please enter some text or number:   ")

if line.lower() == line.lower()[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome")


#or

def palindrome(line):
    line = line.lower().replace(' ', '')
    reversed_line = ''
    for i in range(len(line), 0, -1):
        reversed_line += line[i-1]
    return line == reversed_line

print(palindrome(line))