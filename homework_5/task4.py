# 4) Write a function called send_email that sends an email to a recipient(console output). The function should take a positional argument
# recipient and two keyword arguments: subject and body. The subject argument should have a default value of "Important Message" and
# the body argument should have a default value of an empty string.
def send_email(recipient, subject="Important Message", body=""):
    print(recipient)
    print(subject)
    print(body)


send_email("jane@ukr.net", body="Hello")
