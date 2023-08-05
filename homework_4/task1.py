# Task: Number Guessing Game
# Write a Python program that generates a random number between 1 and 100. Allow the user to guess the number, and provide appropriate feedback (e.g., "Too high" or "Too low") until they guess the correct number. Use a loop and conditional statements to implement the game.
import random

random_number = random.randint(1, 100)
print(random_number)
number_from_user = 0

while random_number != number_from_user:
    number_from_user = int(input("Please guess a number:   "))
    if number_from_user > random_number:
        print("Too high")
    elif number_from_user < random_number:
        print("Too low")
else:
    print("You guessed it!")
