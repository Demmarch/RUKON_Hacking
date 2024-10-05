from flask import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

from secure.main import sanitize_input

import logging


logging.basicConfig(level=logging.DEBUG)

def load_key():
    try:
        with open("secret.key", 'rb') as key_file:
            key = key_file.read()
    except FileNotFoundError:
        key = generate_key()
    return key

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", 'wb') as key_file:
        key_file.write(key)
    return key

key = load_key()
cipher = Fernet(key)

def encrypt_password(password):
    encrypted_password = cipher.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt_password(encrypted_password):
    try:
        decrypted_password = cipher.decrypt(encrypted_password.encode())
        return decrypted_password.decode()
    except Exception as e:
        logging.error(f"Error decrypting password: {e}")
        raise e


app = Flask(__name__)
app.secret_key = "asdkjashdajshaskjdbnanbzc12093872q"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passwords.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    service = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=True)

@app.route("/")
def index():
    if 'user_id' in session:
        return redirect(url_for('main'))
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        username = sanitize_input(request.form.get("username"))
        password = request.form.get("password")

        if len(password) < 15:
            error = 'Пароль должен быть минимум 15 символов!'
            return render_template("reg.html", error=error)

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            error = 'Имя пользователя уже существует!'
            return render_template("reg.html", error=error)

        hashed_password = encrypt_password(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error registering user: {e}")
            error = 'Ошибка регистрации пользователя.'
            return render_template("reg.html", error=error)

        session['user_id'] = new_user.id
        return redirect(url_for('main'))

    return render_template("reg.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = sanitize_input(request.form.get("username"))
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and decrypt_password(user.password) == password:
            session['user_id'] = user.id
            return redirect(url_for('main'))

        error = 'Неверный логин или пароль!'
    return render_template("index.html", error=error)


@app.route("/main")
def main():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))

    passwords = Password.query.filter_by(user_id=user_id).all()
    passwords_info = []

    for password in passwords:
        passwords_info.append({
            'id': password.id,
            'service': sanitize_input(password.service),
            'username': sanitize_input(password.username),
            'password': decrypt_password(password.password)
        })

    return render_template("main.html", passwords=passwords_info)


@app.route("/add_password", methods=["GET", "POST"])
def add_password():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for('login'))
    
    error = None
    if request.method == "POST":
        username = sanitize_input(request.form.get("username"))
        password = request.form.get("password")
        service = sanitize_input(request.form.get("service"))
        desc = sanitize_input(request.form.get("desc"))

        if len(password) < 15:
            error = 'Пароль должен быть минимум 15 символов!'
            return render_template("register_password.html", error=error)
        
        new_password = Password(user_id=user_id, username=username, password=encrypt_password(password), service=service, description=desc)
        db.session.add(new_password)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            app.logger.error(f"Error saving password: {e}")
            error = 'Ошибка сохранения пароля.'
            return render_template("register_password.html", error=error)

        return redirect(url_for('main'))

    return render_template("register_password.html")

@app.route("/update_password", methods=["GET", "POST"])
def update_password():
    user_id = session.get('user_id')
    error = None

    if request.method == "POST":
        if not user_id:
            error = 'Вам необходимо войти в систему для обновления пароля.'
            return redirect(url_for('login'))

        username = sanitize_input(request.form.get("username"))
        service = sanitize_input(request.form.get("service"))
        new_password = request.form.get("password")

        if len(new_password) < 10:
            error = 'Пароль должен быть минимум 10 символов!'
            return render_template("update_password.html", error=error)

        password_entry = Password.query.filter_by(user_id=user_id, username=username, service=service).first()

        if password_entry:
            password_entry.password = encrypt_password(new_password)
            db.session.commit()
            return redirect(url_for('main'))
        else:
            error = 'Пароль не найден.'
            return render_template("update_password.html", error=error)

    return render_template("update_password.html", error=error)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Таблицы созданы")
        
    app.run(port=8000)
