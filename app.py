from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = "smart_waste_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

latest_data = None
last_update = None

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if request.form["email"] == "admin@govt.in" and request.form["password"] == "admin123":
            session["login"] = True
            return redirect("/dashboard")
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

# ESP API
@app.route("/api/update", methods=["POST"])
def update():
    global latest_data, last_update
    latest_data = request.json
    last_update = datetime.now()
    return jsonify({"status": "ok"})

@app.route("/api/data")
def data():
    if not last_update or (datetime.now() - last_update).seconds > 10:
        return jsonify({"connected": False})

    return jsonify({
        "connected": True,
        "data": latest_data
    })

if __name__ == "__main__":
    app.run(debug=True)
