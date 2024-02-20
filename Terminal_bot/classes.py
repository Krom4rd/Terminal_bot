from datetime import date, datetime
from collections import UserDict
import re

def value_error_decorator(inner):
    def wraper(*args):
        try:
            return inner(*args)
        except ValueError:
            print('ValueError')
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
                    print("Date of birthday must be in dd.mm.yyyy or dd-mm-yyyy format")

class Contact():
    def __init__(self, name: Name, phone: Phone = None, email: Email = None, address: Address = None, birthday: Birthday = None):
        self.name = name
        self.phones = []

        if phone is not None:
            new_phone = Phone(phone)
            if new_phone:
                self.phones.append(new_phone)
        if email is not None:
            self.email = Email(email)
        if address is not None:
            self.address = Address(address)
        if birthday is not None:
            self.birthday = Birthday(birthday)
    
    @value_error_decorator
    def add_phone(self, phone_value: str = None):
        new_phone = Phone(phone_value)
        if new_phone is not None:
            self.phones.append(new_phone)
            print(f'Phone: {phone_value} for {self.name} added')
            return True
        else:
            return False

    @value_error_decorator    
    def edit_phone(self, old_phone: str = None, new_phone: str = None):
        for phone in self.phones:
            if phone is not old_phone:
                print(f'{old_phone} not exist')
                return
            new_phone_check = Phone(new_phone)  # валідація нового телефону
            if new_phone_check:
                phone = new_phone
                print(f'Contact {self.name} changed his phone number from {old_phone} to {new_phone}')
    
    @value_error_decorator
    def remove_phone(self, phone_number: str = None):
        for element in self.phones:
            if element.value == phone_number:
                self.phones.remove(element)
                print(f'phone: {phone_number} deleted')
                return    
        print(f'phone {phone_number} not found')

    @value_error_decorator
    def find_phone(self, phone_number: str = None):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None
    
    @value_error_decorator
    def add_birthday(self, birthday: str = None):
        new_birthday = Birthday(birthday)
        if new_birthday is not None:
            self.birthday = new_birthday
            print(f'Birthday: {new_birthday} for {self.name} added')

    @value_error_decorator
    def days_to_birthday(self, days_left):
        contacts_with_birthday = []
        today = datetime.today().date()
        for name in self.name():
            if name.birthday:
                birthday = name.birthday.value
                if isinstance(birthday, str):
                    birthday = datetime.strptime(birthday, '%Y-%m-%d').date()
                this_year_birthday = datetime(today.year, birthday.month, birthday.day).date()
                if this_year_birthday >= today:
                    next_birthday = this_year_birthday
                else:
                    next_birthday = datetime(today.year + 1, birthday.month, birthday.day).date()
                days_until_birthday = (next_birthday - today).days
                if days_until_birthday == days_left:
                    contacts_with_birthday.append(name)
        print(f'The names of those whose birthdays is in {days_left} days: {contacts_with_birthday}')

    @value_error_decorator
    def add_address(self, address: str = None):
        new_address = Address(address)
        if new_address is not None:
            self.address = new_address
            print(f'Address: {new_address} for {self.name} added')

    @value_error_decorator
    def add_email(self, email: str = None):
        new_email = Email(email)
        if new_email is not None:
            self.email = new_email
            print(f'Email: {new_email} for {self.name} added')

    @value_error_decorator
    def edit_email(self, email: str = None):
        new_email = Email(email)
        if new_email is not None:
            old_email = self.email
            self.email = new_email
            print(f'Contact {self.name} change email from {old_email} to {self.email}')

    def __str__(self):
        string = f"Contact name: {self.name}"
        if self.phones:
            string += f', phones: {'; '.join(p.value for p in self.phones)}'
        try:
            if self.email :
                string += f', email: {self.email}'
        except AttributeError:
            pass
        try:
            if self.address:
                string += f', address: {self.address}'
        except AttributeError:
            pass
        try:
            if self.birthday:
                string += f', {self.birthday}'
        except AttributeError:
            pass
        return string
        

class Address_book(UserDict):
    def add_contact(self, contact: Contact):
        self.data[contact.name] = contact

    def remove_contact(self, contact_name: str):
        if contact_name in self.data:
            del self.data[contact_name]

    def search_contact(self, contact_name: str):
        if contact_name in self.data:
            return self.data[contact_name]
        else:
            return None
        
    iter_records = 5

    def __iter__(self):
        self.idx = 0
        self.page = 0
        self.list_of_records = [record for record in self.data]

        return self

    def __next__(self):

        if self.idx >= len(self.data):
            raise StopIteration
        self.count_records = 1
        self.page += 1
        self.result = f'Page: {self.page}'

        while self.count_records <= self.iter_records:
            if self.idx >= len(self.data):
                return self.result
            
            self.result += f'\n{self.data[self.list_of_records[self.idx]]}'
            self.count_records += 1
            self.idx += 1
                
        return self.result
    
    def set_iter_records(self, iter_records):
        self.iter_records = iter_records
   
    def __str__(self):

        if not self.data:
            print('The contact book is empty')
        else:
            self.result = 'Сontacts that are in the contact book:'
            for record in self.data:
                self.result += f'\n{str(self.data[record])}'
            self.result += '\n'

            return self.result

class Note(Field):
    def __init__(self, note: str):
        pass

class Tag(Field):
    def __init__(self, tag: str):
        pass

class Note_book(UserDict):
    def __init__(self, note: Note, tag: Tag = None):
        pass
