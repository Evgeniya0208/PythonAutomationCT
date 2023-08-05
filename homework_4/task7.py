# Task: Vowel Counter
# Write a Python program that takes a string as input from the user and counts the number of vowels (a, e, i, o, u) in the string. Display the result. Use loops and conditional statements to implement this.
line = input("Please input some text:   ")

count = len([char for char in line if char in "aeiouAEIOU"])

print("Number of vowels: ", count   )