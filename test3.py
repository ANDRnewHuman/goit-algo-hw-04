
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
