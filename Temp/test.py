'''
from pathlib import Path


file_name = Path('./Temp')

def total_salary(path):
    total = 0
    count = 0
    file_path = path.resolve() / 'text.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            name, salary = line.strip().split(',')
            total += int(salary)
            count += 1
        if count > 0:
            average = total / count
        else:
            average = 0
    
        return total, average
    


total_salary(file_name)

total, average = total_salary(file_name)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



from pathlib import Path
file_name = Path('./Temp')
def get_cats_info(path):
    cats_info = []
    file_path = Path(path).resolve() / 'text_cat.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) != 3:
                    continue
                
                cat_dict = {
                    "id": cat_data[0],
                    "name": cat_data[1],
                    "age": cat_data[2]
                }
                cats_info.append(cat_dict)
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print("Сталася помилка при читанні файлу:", e)
    
    return cats_info

cats_info = get_cats_info(file_name)
print(cats_info)
'''


def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=2)
    command = parts[0].lower()
    arguments = parts[1:] if len(parts) > 1 else []
    return command, arguments

def add_contact(contacts, arguments):
    if len(arguments) != 2:
        return "Неправильна кількість аргументів. Потрібно ввести ім'я та номер телефону."
    name, phone = arguments
    contacts[name] = phone
    return "Контакт доданий."

def change_contact(contacts, arguments):
    if len(arguments) != 2:
        return "Неправильна кількість аргументів. Потрібно ввести ім'я та новий номер телефону."
    name, new_phone = arguments
    if name in contacts:
        contacts[name] = new_phone
        return "Номер телефону для контакту змінено."
    else:
        return "Контакт з таким ім'ям не знайдено."

def show_phone(contacts, arguments):
    if len(arguments) != 1:
        return "Неправильна кількість аргументів. Потрібно ввести ім'я контакту."
    name = arguments[0]
    if name in contacts:
        return f"Номер телефону для контакту {name}: {contacts[name]}"
    else:
        return "Контакт з таким ім'ям не знайдено."

def show_all(contacts):
    if contacts:
        result = "Список контактів:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result
    else:
        return "Список контактів порожній."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, arguments = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(contacts, arguments))
        elif command == "change":
            print(change_contact(contacts, arguments))
        elif command == "phone":
            print(show_phone(contacts, arguments))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
