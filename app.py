from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "smart_waste_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

latest_data = None

@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@govt.in" and password == "admin123":
            session["login"] = True
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid login")

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
    latest_data = request.json
    return jsonify({"status": "ok"}), 200

@app.route("/api/data")
def data():
    if latest_data is None:
        return jsonify({"connected": False})
    return jsonify({"connected": True, "data": latest_data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
