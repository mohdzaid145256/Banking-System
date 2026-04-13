# 🏦 Banking Web Application

A simple **Banking System Web App** built using **Flask, SQLite, and SQLAlchemy**.
This project allows users to register, login, create accounts, view balances, and transfer money securely.

---

## 🚀 Features

* 🔐 User Registration & Login (with password hashing)
* 🏦 Create Bank Account
* 💰 View Account Balance
* 🔄 Transfer Money Between Accounts
* 🚪 Logout Functionality
* 📊 Total Balance Calculation
* 🛡️ Session-based Authentication

---

## 🛠️ Tech Stack

* **Backend:** Flask
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Authentication:** Werkzeug Security
* **Frontend:** HTML (Templates)

---

## 📂 Project Structure

```
project/
│── app.py
│── bank.db
│── templates/
│   ├── index.html
│   ├── dashboard.html
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mohdzaid145256/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install flask sqlalchemy werkzeug
```

### 4️⃣ Run the Application

```bash
python app.py
```

👉 App will run at:

```
http://127.0.0.1:5000/
```

---

## 🗄️ Database

* Uses **SQLite (bank.db)**
* Automatically created when app runs
* Contains:

  * `customers` table
  * `accounts` table

---

## 🔗 API Endpoints

### 🧑 Register

```
POST /register
```

### 🔐 Login

```
POST /login
```

### 🚪 Logout

```
POST /logout
```

### 🏦 Create Account

```
POST /create-account
```

### 📊 View Accounts

```
GET /accounts
```

### 💸 Transfer Money

```
POST /transfer
```

---

## 🔒 Security Features

* Passwords are hashed using `generate_password_hash`
* Session-based authentication
* Prevents unauthorized dashboard access

---

## 📸 Screens (Optional)

* Home Page
* Dashboard
* Account Overview
* Transfer Interface

---

## 💡 How It Works

* Users register and login
* Session stores user ID
* Users create accounts with initial balance
* Can transfer money between accounts
* All transactions update database in real-time

(Implemented using Flask routes and SQLAlchemy queries )

---

## 🚀 Future Improvements

* Add transaction history
* Improve UI/UX with CSS & animations
* Add email verification
* Use PostgreSQL instead of SQLite
* Deploy on cloud (Render / AWS)

---

## 👨‍💻 Author

**Mohd Zaid**

---

## ⭐ Contribute

Feel free to fork this repo and improve it!

---

## 📜 License

This project is for educational purposes.
