from classes import Address_book, Contact

import pathlib
import pickle

cache = [Address_book()]

# Функція декоратор для обробки помилок
def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "IndexError"
        except ValueError:
            return "ValueError"
        except KeyError:
            return "KeyError"
        except TypeError:
            return "TypeError"
        except ArithmeticError:
            return 'ArithmeticError'
    return wrap


def greeting():
    return "Вітаю! Ласкаво просимо до вашого персонального помічника."

def Capitalize(text):
    # Написаня кожного слова з великої літери
    return ' '.join(word.capitalize() for word in text.split())

def add_contact():
    # Збирання інформації про користувача
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    birthday = input("Enter the birthday (format: dd.mm.yyyy): ")

    
    capitalized_name = Capitalize(name)

    # Створення екземплярів необхідних класів
    contact_name = Name(capitalized_name)
    contact_phone = Phone(phone)
    contact_email = Email(email)
    contact_address = Address(address)
    contact_birthday = Birthday(birthday)

    # Створення "Контакт" із зібраною інформацією
    new_contact = Contact(name=contact_name, phone=contact_phone, email=contact_email, address=contact_address, birthday=contact_birthday)

    # Додавання нового контакту до адресної книги
    address_book.add_contact(new_contact)

    return f"Контакт {capitalized_name} успішно додано до адресної книги."

def change_number(name, old_phone, new_phone): # чи треба вказати contact_name ????
    record = cache.data.get(name)
    if not record:
        raise KeyError(f'Відсутній контакт {name} в адресній книзі')
    for phone in record.phones:
        if phone.value == old_phone:
            phone.value = new_phone
            return f'Ви змінили номер телефону для контакту {name}'
    return f'Відсутній номер {old_phone} в адресній книзі'
    
def phone_output(name): # чи треба вказати contact_name ????
    record = cache.data.get(name)
    if record:
        phones = [phone.value for phone in record.phones]
        return phones
    return 'Відсктній контакт в адресній книзі'

def show_all():
    pass

def delete():
    contact_name = input("Введіть ім'я контакту, який потрібно видалити: ")
    deleted_contact = address_book.search_contact(contact_name)
    
    if deleted_contact:
        address_book.remove_contact(contact_name)
        return f"Контакт {contact_name} успішно видалено з адресної книги."
    else:
        return f"Контакт {contact_name} не знайдено в адресной книзі."


def add_birthday():
    pass

def days_to_birthday():
    pass

def note():
    pass

def add_note():
    pass

def change_note():
    pass

def note_output():
    pass

def delete_note():
    note_id = input("Введіть нотаток, який потрібно видалити: ")
    # Якщо в class Note_book є метод для видалення нотаток
    deleted_note = note_book.remove_note(note_id)

    if deleted_note:
        return f"Note with ID {note_id} успішно видалено із записної книжки."
    else:
        return f"Note with ID {note_id} не знайдено в записній книзі."


def show_all_notes():
    pass

def search_note():
    pass

def tag():
    pass

def add_tag():
    pass

def delete_tag():
    tag_name = input("Введіть назву тегу, який потрібно видалити: ")
    # Якщо в class Note_book є метод для видалення тегів
    deleted_tag = note_book.remove_tag(tag_name)

    if deleted_tag:
        return f"Тег {tag_name} успішно видалено із записної книжки."
    else:
        return f"Тег {tag_name} не знайдено в записній книзі."



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
    greeting: 'hello',
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
    delete_note: 'del note',
    show_all_notes: 'show all notes',
    search_note: 'snote',
    add_tag: 'tag',
    delete_tag: 'del tag',
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