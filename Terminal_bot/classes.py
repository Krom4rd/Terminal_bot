from datetime import date
from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name: str)-> None:
        super().__init__(name.lower().capitalize())

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_number(value):
            return "Invalid phone number format. Try again!"

    def validate_number(self, number):
        return len(number) == 10 and number.isdigit()
    
class Email(Field):
    def __init__(self, mail: str):
        super().__init__(mail)
        if not self.validate_email(mail):
            return "Invalid email format. Try again!"

    def validate_email(self, mail):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, mail):
            return True
        else:
            return False

class Address(Field):
    def __init__(self, address: str):
        pass

class Birthday(Field):
    def __init__(self, day: str):
        pass

class Contact():
    def __init__(self, name: Name, phone: Phone = None, email: Email = None, address: Address = None, birthday: Birthday = None):
        pass

class Address_book(UserDict):
    pass

class Note(Field):
    def __init__(self, note: str):
        pass

class Tag(Field):
    def __init__(self, tag: str):
        pass

class Note_book(UserDict):
    def __init__(self, note: Note, tag: Tag = None):
        pass

