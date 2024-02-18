from datetime import date, datetime
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
        return str(self.value)

class Name(Field):
    def __init__(self, name: str)-> None:
        super().__init__(name.lower().capitalize())

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not self.validate_number(value):
            print("Invalid phone number format. Try again!")

    def validate_number(self, number):
        return len(number) == 10 and number.isdigit()

class Email(Field):
    def __init__(self, mail: str):
        super().__init__(mail)
        if not self.validate_email(mail):
            print("Invalid email format. Try again!")

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
    @Field.value.setter
    def value(self, value: str = None):
        if value == None:
            self._value = ''
        else:
            try:
            # Спроба перетворити введене значення на об'єкт date
                self._value = datetime.strptime(value, '%d.%m.%Y').date()
            except ValueError:
                try:
                # Якщо перша спроба не вдалася, то спробуємо інший формат дати
                    self._value = datetime.strptime(value, '%d-%m-%Y').date()
                except ValueError:
                # Якщо жоден з форматів не підходить, пишемо про помилку
class-Birthday
                    print("Значення повинно бути в форматі dd.mm.yyyy або dd-mm-yyyy")

class Contact():
    def __init__(self, name: Name, phone: Phone = None, email: Email = None, address: Address = None, birthday: Birthday = None):
        self.name = name
        
        if phone is not None:
            self.phone = Phone(phone)
        if email is not None:
            self.email = Email(email)
        if address is not None:
            self.address = Address(address)
        if birthday is not None:
            self.birthday = Birthday(birthday)
    
    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        if phone != None:
            self.phones.append(phone)
            return True
        else:
            return False

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

