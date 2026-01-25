from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "smart_waste_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

latest_data = {
    "bin_id": "-",
    "area": "-",
    "gas": 0,
    "level": 0,
    "status": "OFFLINE"
}

@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["email"] == "admin@govt.in" and request.form["password"] == "admin123":
            session["login"] = True
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid Login")
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

# -------- ESP API --------
@app.route("/api/update", methods=["POST"])
def update():
    global latest_data
    data = request.json

    level = int(data.get("level", 0))
    gas = int(data.get("gas", 0))

    if level >= 90 or gas >= 300:
        status = "CRITICAL"
    elif level >= 60:
        status = "WARNING"
    else:
        status = "NORMAL"

    latest_data = {
        "bin_id": data.get("bin_id"),
        "area": data.get("area"),
        "gas": gas,
        "level": level,
        "status": status
    }

    return jsonify({"message": "OK"}), 200

@app.route("/api/data")
def data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


