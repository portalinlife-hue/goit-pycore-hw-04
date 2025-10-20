def parse_input(user_input):
    """
    Розбирає введений рядок на команду та аргументи.
    """
    # Розділяє рядок на слова, перше слово - команда, решта - аргументи
    parts = user_input.split()
    command = parts[0].strip().lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника.
    Повертає рядок з підтвердженням або повідомленням про помилку.
    """
    # Перевіряємо, чи передано рівно два аргументи (ім'я та телефон)
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону існуючого контакту.
    """
    if len(args) != 2:
        return "Invalid command format. Use: change [name] [phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """
    Показує номер телефону для вказаного контакту.
    """
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "No contacts saved yet."
    
    # Створюємо гарно відформатований рядок для виводу
    contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contact_list

def main():
    """
    Головна функція, що керує циклом обробки команд бота.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        # Отримуємо ввід від користувача та очищуємо його від зайвих пробілів
        user_input = input("Enter a command: ").strip()
        
        # Якщо користувач нічого не ввів, продовжуємо цикл
        if not user_input:
            continue
            
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
            
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            # Виправлено: передаємо тільки contacts
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()