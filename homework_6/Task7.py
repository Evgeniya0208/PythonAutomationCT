class Contact:

    def __init__(self, first_name, last_name, phone_number, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        self._email = value

contact = Contact("Helen", "Smith", "+38093132323", email="helen@ukr.net")
print(contact.first_name)
print(contact.last_name)
print(contact.phone_number)
print(contact.email)