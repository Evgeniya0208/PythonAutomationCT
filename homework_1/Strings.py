# 4) Create three strings using different quotes
singleQuoteString = 'The field should be empty.'
print(singleQuoteString)

doubleQuotesString = "The {field} field should contain {value}."
print(doubleQuotesString.format(field="Name", value="Marry O'Brien"))

tripleQuotesString = """It’s easy when conveying system errors to turn into a robot, but the best thing you can do is 
fight for your humanity. Making your error messages human and friendly humanizes the brand and makes it feel more like 
you care. Users prefer getting help from a person, and being friendly can remove frustration and generate understanding."""
print(tripleQuotesString)

# 5) Given a string - “Hello, this is just a simple string for testing”. Make this string lower-cased, reverse all the separate words and take the last word out of it. Assign this word to a variable.
my_string = "Hello, this is just a simple string for testing"
print(my_string.lower())
print(my_string[::-1])
new_string = my_string[::-1].split(',')[-1]
print(new_string)

# 6) Given a url:
# ‘https://localhost:8080/query?username=Dmytro&phone=1234567890
# Using string methods extract from this url username and phone number and assign them to the separate variables ‘username’ and ‘phone’ accordingly
url = "https://localhost:8080/query?username=Dmytro&phone=1234567890"
usernameStartIndex = url.find('username=') + len('username=')
usernameEndIndex = url.find('&')
phoneStartIndex = url.find('phone=') + len('phone=')

username = url[usernameStartIndex:usernameEndIndex]
phone = url[phoneStartIndex:]

print(username)
print(phone)
