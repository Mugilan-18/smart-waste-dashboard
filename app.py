from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "smart_waste_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

latest_data = None
connected = False

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
def update_data():
    global latest_data, connected
    latest_data = request.json
    connected = True
    return jsonify({"status": "received"}), 200

@app.route("/api/data")
def get_data():
    if not connected or not latest_data:
        return jsonify({
            "connected": False,
            "total_bins": 0,
            "message": "No ESP Data received yet"
        })
    return jsonify({
        "connected": True,
        "total_bins": latest_data.get("total_bins", 0),
        "data": latest_data.get("data", {})
    })

if __name__ == "__main__":
    app.run(debug=True)
