from datetime import date
from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self)->str:
        return self._value

    @value.setter
    def value(self, value: str)-> None:
        self._value = value

    def __str__(self):
        return str(self._value)

class Name(Field):
    def __init__(self, name: str)-> None:
        super().__init__(name.lower().capitalize())

class Phone(Field):
    def __init__(self, number: str):
        pass

class Email(Field):
    def __init__(self, mail: str):
        pass

class Address(Field):
    def __init__(self, address: str):
        pass

class Birthday(Field):
    def __init__(self, day: str):
        pass

class Contact():
    def __init__(self, name: Name, phone: Phone = None, email: Email = None, address: Address = None, birthday: Birthday = None):
        pass

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                new_phone_check = Phone(new_phone)
                new_phone_check.validate(new_phone)   # валідація нового телефону
                phone.value = new_phone
                return       
        return ValueError(f'{old_phone} not exist')
    
    def remove_phone(self, phone_number):
        for element in self.phones:
            if element.value == phone_number:
                self.phones.remove(element)
                return f'phone: {phone_number} deleted'
            return f'phone {phone_number} not found'

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

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

