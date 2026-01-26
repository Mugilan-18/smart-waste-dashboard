from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "smart_waste_secret"

latest_data = None
last_seen = None

@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
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

@app.route("/api/update", methods=["POST"])
def update():
    global latest_data, last_seen
    latest_data = request.json
    last_seen = datetime.now()
    return jsonify({"ok": True})

@app.route("/api/data")
def data():
    if not latest_data:
        return jsonify({"system_status": "OFFLINE"})

    offline = datetime.now() - last_seen > timedelta(seconds=8)

    return jsonify({
        "bin_id": latest_data["bin_id"],
        "area": latest_data["area"],
        "gas": latest_data["gas"],
        "bin_level": latest_data["bin_level"],
        "system_status": "OFFLINE" if offline else "ONLINE",
        "monitoring": "LIVE" if not offline else "STOPPED"
    })

if __name__ == "__main__":
    app.run()




