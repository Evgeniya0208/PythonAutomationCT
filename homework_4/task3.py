# Task: Password Strength Checker
# Write a Python program that takes a password as input from the user and checks its strength. Display a message indicating whether the password is weak, moderate, or strong based on the following criteria:
# Weak: Less than 8 characters long
# Moderate: 8 to 12 characters long
# Strong: More than 12 characters long
# Use conditional statements to determine the strength.
password = input("Please enter new password:   ")

if len(password) < 8:
    print("This password is weak")
elif 8 <= len(password) <= 12:
    print("This password is moderate")
elif len(password) > 12:
    print("This password is strong")
