# 📇 Contact Manager using Python & SQLite

A simple contact management system built with **Python** and **SQLite**, allowing users to **add**, **view**, **update**, and **delete** contacts. Each contact includes a **name**, **phone number**, and **email address**.

---

## 🛠️ Features

- Add new contacts  
- View all saved contacts  
- Update existing contacts  
- Delete a contact  
- Persistent storage using SQLite  
- Console-based user interface

---

## 📂 Project Structure

```
contact_manager/
│
├── contact_manager.py         # Main Python script
├── contacts.db                # SQLite database (auto-created)
├── README.md                  # Project description
└── requirements.txt           # Dependencies (if any)
```

---

## ▶️ How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/Ayushgowda27/contact_manager.git
cd contact_manager
```

2. **Run the Script**
```bash
python contact_manager.py
```

3. **Follow the Menu Options:**
- 1: Add Contact  
- 2: View Contacts  
- 3: Update Contact  
- 4: Delete Contact  
- 5: Exit  

---


---

## 🗃️ SQLite Database

SQLite is used for storing contact data persistently. The `contacts.db` database is created automatically when you first run the script. It contains a table:

```sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
);
```

---

## 🧪 Requirements

No external packages required — works with standard Python libraries:
```
sqlite3
```

If using enhanced input or color libraries, add them to `requirements.txt`:
```
colorama  # Optional
```

---

## 🧑‍💻 Author

**Ayush Gowda**

---

## 📬 Contact

For questions or feedback, feel free to reach out via:
- GitHub Issues: [Open Issue](https://github.com/Ayushgowda27/contact_manager/issues)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
