import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ----- DB Setup -----
def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

def fetch_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_contact(name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

def update_contact(contact_id, name, phone, email):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?", (name, phone, email, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()

# ----- GUI Setup -----
def refresh_contacts():
    for row in contact_list.get_children():
        contact_list.delete(row)
    for contact in fetch_contacts():
        contact_list.insert("", tk.END, values=contact)

def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()
    if name and phone and email:
        insert_contact(name, phone, email)
        refresh_contacts()
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def select_contact(event):
    selected = contact_list.selection()
    if selected:
        values = contact_list.item(selected[0])['values']
        contact_id_var.set(values[0])
        name_var.set(values[1])
        phone_var.set(values[2])
        email_var.set(values[3])

def edit_contact():
    contact_id = contact_id_var.get()
    if contact_id:
        update_contact(contact_id, name_var.get(), phone_var.get(), email_var.get())
        refresh_contacts()
        clear_fields()

def remove_contact():
    contact_id = contact_id_var.get()
    if contact_id:
        delete_contact(contact_id)
        refresh_contacts()
        clear_fields()

def clear_fields():
    contact_id_var.set("")
    name_var.set("")
    phone_var.set("")
    email_var.set("")

# ----- Main -----
init_db()

root = tk.Tk()
root.title("Contact Manager")
root.geometry("600x400")

# Variables
contact_id_var = tk.IntVar()
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

# Entry Form
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
tk.Entry(frame, textvariable=name_var).grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0)
tk.Entry(frame, textvariable=phone_var).grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0)
tk.Entry(frame, textvariable=email_var).grid(row=2, column=1)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=edit_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=remove_contact).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Clear", command=clear_fields).grid(row=0, column=3, padx=5)

# Contact List
columns = ("ID", "Name", "Phone", "Email")
contact_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    contact_list.heading(col, text=col)
    contact_list.column(col, width=100)
contact_list.pack(fill="both", expand=True)
contact_list.bind("<<TreeviewSelect>>", select_contact)

refresh_contacts()

root.mainloop()
