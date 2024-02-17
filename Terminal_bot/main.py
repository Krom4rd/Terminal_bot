from classes import Address_book, Contact, Note
from datetime import datetime

import pathlib
import pickle

# cache = [Address_book(),Note()]

def greating():
    pass

def add_contact():
    pass

def change_number():
    pass

def phone_output():
    pass

def show_all():
    pass

def delete():
    pass

def add_birthday():
    pass
        
def days_to_birthday(birthday):
    if birthday:
        if isinstance(birthday, str):
            birthday = datetime.strptime(birthday, '%Y-%m-%d')
            
        today = datetime.today()
        birthday_this_year = datetime(today.year, birthday.month, birthday.day)
        if birthday_this_year >= today:
            next_birthday = birthday_this_year
        else:
            next_birthday = datetime(today.year + 1, birthday.month, birthday.day)
        days_left = (next_birthday - today).days
        return days_left
    else:
        return None

def note():
    pass

def add_note():
    pass

def change_note():
    pass

def note_output():
    pass

def delete_note():
    pass

def show_all_notes():
    pass

def search_note():
    pass

def tag():
    pass

def add_tag():
    pass

def delete_tag():
    pass

def about():
    pass

def sorting():
    pass

# Функція для запису кешу в окремий файл для зберігання данних
def exit(data):
    # Якщо кеш пустий та окремий файл для зберігання існує тоді файл буде видалено
    if not cache and pathlib.Path('cache.bin').exists():
        pathlib.Path('cache.bin').unlink()
        return None
    with open('cache.bin', 'wb') as file:
        pickle.dump(cache, file)

# Функія для відновлення кешу при повторному виклику програми
def return_cache():
    with open('cache.bin', 'rb') as file:
        global cache
        cache = pickle.load(file)

# Словник ключ = Функція, значення= Ключові слова для запуску функцій
COMMANDS = {
    greating: 'hello',
    add_contact: 'add',
    change_number: 'change',
    phone_output: 'phone',
    show_all: 'show all',
    exit: ['exit', 'good bye', 'close'],
    delete: 'delete',
    about: 'about',
    add_birthday: 'birthday',
    days_to_birthday: 'days to birthday',
    add_note: 'note',
    delete_note: 'del_note',
    show_all_notes: 'show all notes',
    search_note: 'snote',
    add_tag: 'tag',
    delete_tag: 'del_tag',
    sorting: 'sorting'
}

def commands(data):
    pass

def main():
    # Якщо раніше використовувалася програма та було створено кеш: його буде відновлено
    if pathlib.Path('cache.bin').exists():
        return_cache()
    # Цикл для тривалої роботи програми
    while True:
        # Отримання даних від користувачаa
        user_input = input('>>>')
        if user_input:
            func, data = commands(user_input)
        if func == None:
            continue
        elif func == exit:
            # Вихід з програми та запис кешу в окремий файл
            func(data)
            print('Good bye')
            break
        else:
            # Запуск команд
            result = func(data)
            print(result)

if __name__ == '__main__':
    main()