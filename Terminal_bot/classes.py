from datetime import date, datetime
from collections import UserDict
import re

def value_error_decorator(inner):
    def wraper(*args):
        try:
            return inner(*args)
        except ValueError:
            return 'ValueError'
    return wraper

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
        super().__init__(address)

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
    
    @value_error_decorator
    def add_phone(self, phone_value):
        phone = Phone(phone_value)
        if phone != None:
            self.phones.append(phone)
            return True
        else:
            return False

    @value_error_decorator    
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                new_phone_check = Phone(new_phone)
                new_phone_check.validate(new_phone)   # валідація нового телефону
                phone.value = new_phone
                return       
        return ValueError(f'{old_phone} not exist')
    
    @value_error_decorator
    def remove_phone(self, phone_number):
        for element in self.phones:
            if element.value == phone_number:
                self.phones.remove(element)
                return f'phone: {phone_number} deleted'
            return f'phone {phone_number} not found'

    @value_error_decorator
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    @value_error_decorator
    def add_birthday(self, birthday: str = None):
        new_birthday = Birthday(birthday)
        if new_birthday is not None:
            self.birthday = new_birthday

    @value_error_decorator
    def add_address(self, address):
        new_address = Address(address)
        if new_address is not None:
            self.address = new_address

    @value_error_decorator
    def add_email(self, email):
        new_email = Email(email)
        if new_email is not None:
            self.email = new_email

    @value_error_decorator
    def edit_email(self, email):
        new_email = Email(email)
        if new_email is not None:
            old_email = self.email
            self.email = new_email
            print(f'Contact {self.name} change email from {old_email} to {self.email}')
        
    

class Address_book(UserDict):
    def __init__(self):
        super().__init__()

    def add_contact(self, contact: Contact):
        self.data[contact.name.value] = contact

    def remove_contact(self, contact_name: str):
        if contact_name in self.data:
            del self.data[contact_name]

    def search_contact(self, contact_name: str):
        if contact_name in self.data:
            return self.data[contact_name]
        else:
            return None

class Note(Field):
    def __init__(self, note: str):
        pass

class Tag(Field):
    def __init__(self, tag: str):
        pass

class Note_book(UserDict):
    def __init__(self, note: Note, tag: Tag = None):
        pass

