

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if contacts.get(name) is None:
        return "contact not found"
    else:
        contacts[name] = phone
        return "contact has been changed"
    
def get_phone(args, contacts):
    name = args[0]
    if contacts.get(name) is None:
        return "contact not found"
    else:
        return contacts.get(name)
    
def find_all(contacts):
    if len(contacts) == 0:
        return "contact's book is empty"
    else:
        info = "contact book:"
        for name, phone in contacts.items():
            info += f"\nname {name} phone {phone}"
        return info


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(get_phone(args, contacts))
        elif command == "all":
            print(find_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
