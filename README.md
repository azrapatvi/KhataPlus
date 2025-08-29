# 📒 KhataPlus – Personal Ledger Web App

**KhataPlus** is a simple web application built with **Flask + MySQL** to manage personal and business ledgers.  
It helps users keep track of transactions, balances, customers, and monthly reports in a digital way.

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
│── app.py # Main Flask application
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

## 🎯 Purpose

KhataPlus is made for **shopkeepers, small businesses, and individuals** who want a **digital ledger system** instead of keeping manual notebooks.  
It works like a **smart khata book** with clear records, quick balances, and easy reports.
