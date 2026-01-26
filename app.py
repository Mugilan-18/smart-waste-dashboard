from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import timedelta
import time

app = Flask(__name__)
app.secret_key = "smart_waste_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

latest_data = None
last_update = 0

@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["email"] == "admin@govt.in" and request.form["password"] == "admin123":
            session["login"] = True
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid Login Credentials")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("login"):
        return redirect("/login")
    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------- ESP DATA API ----------
@app.route("/api/update", methods=["POST"])
def update():
    global latest_data, last_update
    latest_data = request.json
    last_update = time.time()
    return jsonify({"status":"ok"})

@app.route("/api/data")
def data():
    if not latest_data or time.time() - last_update > 10:
        return jsonify({"connected": False})
    return jsonify({"connected": True, "data": latest_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
