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

class Address_book(UserDict):
    pass

class Note(Field):
    def __init__(self, note: str):
        pass

class Tag(Field):
    def __init__(self, tag: str):
        pass


