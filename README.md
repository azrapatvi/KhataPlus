# 📒 KhataPlus – Personal Ledger Web App

**KhataPlus** is a simple web application built with **Flask + MySQL** to manage personal and business ledgers.  
It helps users keep track of transactions, balances, customers, and monthly reports in a digital way.

---

## 💡 Inspiration Behind KhataPlus  

The idea of creating **KhataPlus** came from my father.  
I often saw him managing records in traditional notebooks, and whenever he had to find a particular person’s entry, it became time-consuming and difficult.  

To solve this problem, I came up with the idea of **digitizing the ledger system** – making it faster, searchable, and more reliable.  

That’s how **KhataPlus** was born: a modern version of a notebook ledger that saves time and effort.

---

## 🎯 Purpose  

KhataPlus is made for **shopkeepers, small businesses, and individuals** who want a **digital ledger system** instead of keeping manual notebooks.  
It works like a **smart khata book** with:  
- Clear records  
- Quick balances  
- Easy reports  
- Simple tracking of payments  

---

## 🚀 Features  

- 🔐 **User Accounts** – Register, log in, and log out securely  
- 👤 **Personal Ledger** – Each user gets their own ledger table  
- ➕ **Add Transactions** – Record name, date, amount, and notes  
- 📊 **Balances Page** – See all entries with options to edit or delete  
- 🧾 **Users Page** – View all customers linked to your account with their full transaction history  
- 💵 **Payment Tracking** – Keep track of payments and pending amounts  
- 📅 **Reports** – Monthly summary of total transactions  
- 🖥️ **Simple UI** – Clean design with search, filters, and pagination (Bootstrap + DataTables)  

---

## 🛠️ Tech Stack  

- **Backend:** Flask (Python)  
- **Database:** MySQL  
- **Frontend:** HTML, Bootstrap, DataTables (jQuery)  
- **Authentication:** Werkzeug Security (Password Hashing)  

---

## 📂 Project Structure  


```
KhataPlus/
│── main.py # Main Flask application
│── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── add_entry.html
│ ├── balances.html
│ ├── users.html
│ ├── reports.html
│ └── update.html
│── static/ # Static files (CSS, JS if any)
│── requirements.txt # Python dependencies
│── README.md # Project documentation
```

## 📖 How It Works  

1. **Register an Account** – Create your account with name, email, and password.  
2. **Login** – Access your personal ledger.  
3. **Add Transactions** – Record entries with name, date, amount, and notes.  
4. **Check Balances** – View all your entries with edit/delete options.  
5. **Users Page** – See all customers you have added and view their histories.  
6. **Reports** – Generate monthly summaries to know total transactions.  
7. **Logout** – Securely sign out when done.  

