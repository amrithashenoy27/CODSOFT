contacts = {}

while True:
    print("=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print(f"Contact added successfully!\n")
    elif choice == "2":
        if contacts:
            print("Contact List:")
            for name, info in contacts.items():
                print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
        else:
            print("No contacts available.\n")

    elif choice == "3":
        search_name = input("Enter name or phone number to search: ")
        found = False
        for name, info in contacts.items():
            if search_name == name or search_name == info['Phone']:
                print(
                    f"Found Contact - Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}, Address: {info['Address']}")
                found = True
                break
        if not found:
            print("Contact not found.\n")

    elif choice == "4":
        update_contact = input("Enter the name of the contact to update: ")
        if update_contact in contacts:
            print("Updating contact details. Press Enter to skip updating a field.")
            phone = input(f"Enter new phone number (current: {contacts[update_contact]['Phone']}): ") or contacts[update_contact]['Phone']
            email = input(f"Enter new email (current: {contacts[update_contact]['Email']}): ") or contacts[update_contact]['Email']
            address = input(f"Enter new address (current: {contacts[update_contact]['Address']}): ") or contacts[update_contact]['Address']
            contacts[update_contact] = {'Phone': phone, 'Email': email, 'Address': address}
            print(f"Contact {update_contact} updated successfully!\n")
        else:
            print(f"Contact {update_contact} not found.\n")

    elif choice == "5":
        name = input("Enter the name of the contact to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully!\n")
        else:
            print(f"Contact {name} not found.\n")

    elif choice == "6":
        print("Exiting the contact book.")
        break

    else:
        print("Invalid choice! Please enter a valid option.\n")
