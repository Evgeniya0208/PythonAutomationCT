# Task 4: File Copying
# Write a Python program that reads the contents of a source file named "source.txt" and copies them to a destination file named "destination.txt".
with open("source.txt", 'r') as source, open("destination.txt", 'a') as destination:
    for line in source:
        destination.write(line)