class Contact:

    def __init__(self, first_name, last_name, phone_number, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        self._first_name = value

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, value):
        self._last_name = value

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, value):
        self._phone_number = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

contact = Contact("Helen", "Smith", "+38093132323", email="helen@ukr.net")
print(contact.get_email())
contact.set_email("helen2@ukr.net")
print(contact.get_email())