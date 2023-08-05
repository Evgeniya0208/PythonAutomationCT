# Task: Character Counter
# Write a Python program that takes a string as input from the user and counts the number of occurrences of each character in the string. Display the result in the format: "Character: Count". Use loops and conditional statements to implement this.
line = input("Please input some text:   ")

my_dict = dict()

for character in line:
    count = line.count(character)
    my_dict[character] = count
for key, value in my_dict.items():
    print(key, value)


#or
my_set = set(line)
count_of_chars = dict()

for element in my_set:
    count_of_char = 0
    for character in line:
        if character == element:
            count_of_char += 1
    count_of_chars[element] = count_of_char
for key, value in count_of_chars.items():
        print(key, value)



