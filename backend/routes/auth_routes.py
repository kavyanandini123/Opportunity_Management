from flask import request, jsonify
from app import app
from models import db, Admin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
import secrets
import re


# =========================
# ✅ SIGNUP
# =========================
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json

    print("Signup data:", data)

    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirm_password')

    # 🔹 Validate required fields
    if not all([full_name, email, password, confirm_password]):
        return jsonify({"error": "All fields are required"}), 400

    # 🔹 Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400

    # 🔹 Password length
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    # 🔹 Password match
    if password != confirm_password:
        return jsonify({"error": "Passwords do not match"}), 400

    # 🔹 Check if user exists
    if Admin.query.filter_by(email=email).first():
        return jsonify({"error": "Account already exists"}), 400

    # 🔹 Hash password
    hashed_password = generate_password_hash(password)

    # 🔹 Save to DB
    new_admin = Admin(
        full_name=full_name,
        email=email,
        password_hash=hashed_password
    )

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({"message": "Signup successful"}), 201


# =========================
# ✅ LOGIN
# =========================
@app.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')
    remember = data.get('remember', False)

    # 🔹 Find user
    user = Admin.query.filter_by(email=email).first()

    # 🔹 Validate credentials
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    # 🔹 Login user
    login_user(user, remember=remember)

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email
        }
    }), 200


# =========================
# ✅ FORGOT PASSWORD
# =========================
@app.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')

    user = Admin.query.filter_by(email=email).first()

    if user:
        # Generate token (valid for demo)
        token = secrets.token_urlsafe(16)

        # In real app → store token with expiry
        print(f"Reset link (valid 1 hour): http://localhost:5000/reset/{token}")

    # 🔹 Always same response (security)
    return jsonify({
        "message": "If the email exists, a reset link has been sent"
    }), 200