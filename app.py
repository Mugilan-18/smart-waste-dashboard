from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "smart_waste_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

latest_data = None

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@govt.in" and password == "admin123":
            session["login"] = True
            return redirect("/dashboard")
        return render_template("login.html", error="Invalid Credentials")

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

# ---------- ESP API ----------
@app.route("/api/update", methods=["POST"])
def update():
    global latest_data
    data = request.json

    gas = int(data.get("gas", 0))
    level = int(data.get("level", 0))

    if gas >= 400 or level >= 90:
        status = "CRITICAL"
    elif gas >= 250 or level >= 60:
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
    return jsonify({"msg": "ok"})

@app.route("/api/data")
def data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(debug=True)





