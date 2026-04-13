from flask import Flask, request, jsonify, render_template, session as flask_session
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")

# ================= DATABASE =================
engine = create_engine("sqlite:///bank.db")
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

customers = Table("customers", metadata,
    Column("customer_id", Integer, primary_key=True),
    Column("name", String),
    Column("email", String, unique=True),
    Column("password", String)
)

accounts = Table("accounts", metadata,
    Column("account_id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.customer_id")),
    Column("balance", Float),
    Column("status", String)
)

metadata.create_all(engine)

# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in flask_session:
        return "Login first", 401
    return render_template("dashboard.html")

# ================= REGISTER =================
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name").strip()
    email = data.get("email").strip()
    password = data.get("password").strip()

    hashed = generate_password_hash(password)

    existing = session.execute(
        customers.select().where(customers.c.email == email)
    ).fetchone()

    if existing:
        return jsonify({"error": "Email exists"}), 400

    session.execute(customers.insert().values(
        name=name,
        email=email,
        password=hashed
    ))
    session.commit()

    return jsonify({"message": "Registered successfully"})

# ================= LOGIN =================
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email").strip()
    password = data.get("password").strip()

    user = session.execute(
        customers.select().where(customers.c.email == email)
    ).fetchone()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Wrong password"}), 401

    flask_session["user"] = user.customer_id
    return jsonify({"message": "Login successful"})

# ================= LOGOUT =================
@app.route("/logout", methods=["POST"])
def logout():
    flask_session.clear()
    return jsonify({"message": "Logged out"})

# ================= CREATE ACCOUNT =================
@app.route("/create-account", methods=["POST"])
def create_account():
    user_id = flask_session.get("user")

    session.execute(accounts.insert().values(
        customer_id=user_id,
        balance=1000,
        status="Active"
    ))
    session.commit()

    return jsonify({"message": "Account created"})

# ================= VIEW ACCOUNTS =================
@app.route("/accounts")
def accounts_view():
    user_id = flask_session.get("user")

    result = session.execute(
        accounts.select().where(accounts.c.customer_id == user_id)
    ).fetchall()

    accs = [{"account_id": r.account_id, "balance": r.balance} for r in result]
    total = sum(a["balance"] for a in accs)

    return jsonify({"accounts": accs, "total_balance": total})

# ================= TRANSFER =================
@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.json
    user_id = flask_session.get("user")

    from_acc = int(data["from_account"])
    to_acc = int(data["to_account"])
    amount = float(data["amount"])

    sender = session.execute(
        accounts.select().where(
            (accounts.c.account_id == from_acc) &
            (accounts.c.customer_id == user_id)
        )
    ).fetchone()

    receiver = session.execute(
        accounts.select().where(accounts.c.account_id == to_acc)
    ).fetchone()

    if not sender or not receiver:
        return jsonify({"error": "Invalid account"}), 400

    if sender.balance < amount:
        return jsonify({"error": "Insufficient balance"}), 400

    session.execute(
        accounts.update().where(accounts.c.account_id == from_acc)
        .values(balance=sender.balance - amount)
    )

    session.execute(
        accounts.update().where(accounts.c.account_id == to_acc)
        .values(balance=receiver.balance + amount)
    )

    session.commit()

    return jsonify({"message": "Transfer successful"})

if __name__ == "__main__":
    app.run(debug=True)
