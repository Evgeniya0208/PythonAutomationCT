# Task 2: File Writing
# Write a Python program that prompts the user to enter some text and saves it to a text file named "output.txt".

text = input("Please enter some text!!   ")
try:
    with open('output.txt', 'w') as output:
        output.write(text)
except Exception as e:
    print("There is a Problem", str(e))