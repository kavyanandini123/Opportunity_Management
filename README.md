# 🌐 Opportunity Management System

## 📌 Overview

The Opportunity Management System is a full-stack web application built using Flask.
It allows administrators to manage opportunities with full CRUD operations along with authentication.

---

## 🚀 Features

- 🔐 User Authentication (Signup & Login)
- ➕ Add Opportunities
- 📋 View Opportunities
- ✏️ Edit Opportunities
- ❌ Delete Opportunities
- 📊 Dashboard UI
- 💾 SQLite database integration

---

## 🛠️ Tech Stack

**Frontend:**

- HTML
- CSS
- JavaScript

**Backend:**

- Python (Flask)
- SQLAlchemy
- Flask-Login
- Flask-CORS

**Database:**

- SQLite

---

## 📂 Project Structure

```plaintext
backend/
│── app.py
│── config.py
│── models.py
│── requirements.txt
│── routes/
│   ├── auth_routes.py
│   ├── opportunity_routes.py
│── admin.html
│── admin.css
│── admin.js
│── instance/
│── utils/

README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/opportunity-management-system.git
cd opportunity-management-system/backend
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the application

```bash
python app.py
```

---

### 5️⃣ Open in browser

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

- Flask serves both backend APIs and frontend files.
- HTML, CSS, and JavaScript are rendered using Flask.
- API calls are handled using `fetch`.
- SQLAlchemy manages database operations.
- Data is stored in SQLite.

---

## 🌍 Deployment

You can deploy this project using:

- **Render (Backend + Frontend together)**
- No separate frontend deployment required

---

## 📸 Screenshots

(Add screenshots here)

---

## 🎯 Future Improvements

- Search and filter options
- Pagination
- Better UI enhancements
- Cloud database integration

---

## 👩‍💻 Author

Kavyanandini Mutyala

---

## ⭐ Acknowledgements

This project was built as part of learning full-stack development using Flask.
