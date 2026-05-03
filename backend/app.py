from flask import Flask, send_from_directory
from config import Config
from models import db, Admin
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

# Initialize DB
db.init_app(app)

# Enable CORS
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


# =========================
# ✅ CREATE DATABASE (FIX)
# =========================
with app.app_context():
    db.create_all()


# =========================
# 🏠 Serve HTML
# =========================
@app.route('/')
def home():
    return send_from_directory('.', 'admin.html')


# =========================
# 🎨 Serve CSS
# =========================
@app.route('/admin.css')
def serve_css():
    return send_from_directory('.', 'admin.css')


# =========================
# ⚙️ Serve JS
# =========================
@app.route('/admin.js')
def serve_js():
    return send_from_directory('.', 'admin.js')


# =========================
# 🔗 Import routes
# =========================
from routes.auth_routes import *
from routes.opportunity_routes import *


# =========================
# 🚀 Run app
# =========================
if __name__ == "__main__":
    app.run(debug=True)