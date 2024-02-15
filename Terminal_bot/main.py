import classes

import pathlib
import pickle

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

def days_to_birthday():
    pass

def note():
    pass

def tag():
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
    note: 'note',
    tag: 'tag',
    sorting: 'sorting'
}

def main():
    pass

if __name__ == '__main__':
    main()