import json

class ContactBook:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact {name} added.")

    def view_contacts(self):
        print("\nContact List:")
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        print()

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        print()
    
    def update_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                print(f"Updating contact: {contact['name']}")
                contact['name'] = input("Enter new name: ")
                contact['phone'] = input("Enter new phone number: ")
                contact['email'] = input("Enter new email: ")
                contact['address'] = input("Enter new address: ")
                self.save_contacts()
                print(f"Contact {contact['name']} updated.")
                return
        print("Contact not found.")

    def delete_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact['name'].lower() or query in contact['phone']:
                self.contacts.remove(contact)
                self.save_contacts()
                print(f"Contact {contact['name']} deleted.")
                return
        print("Contact not found.")

def main():
    book = ContactBook()

    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone, email, address)
        elif choice == '2':
            book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            book.search_contact(query)
        elif choice == '4':
            query = input("Enter name or phone number to update: ")
            book.update_contact(query)
        elif choice == '5':
            query = input("Enter name or phone number to delete: ")
            book.delete_contact(query)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
