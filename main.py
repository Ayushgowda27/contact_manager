import sqlite3

# ----- Database Setup -----
def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

# ----- Add Contact -----
def add_contact(name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
    print("Contact added.")

# ----- View Contacts -----
def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# ----- Edit Contact -----
def edit_contact(contact_id, name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()
    print("Contact updated.")

# ----- Delete Contact -----
def delete_contact(contact_id):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()
    print("Contact deleted.")

# ----- Main Menu -----
def main():
    init_db()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            contact_id = int(input("Enter contact ID to edit: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            edit_contact(contact_id, name, phone, email)
        elif choice == "4":
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
