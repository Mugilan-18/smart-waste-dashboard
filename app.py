from flask import Flask, render_template, request, redirect, session, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "smart_waste_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

latest_data = None
last_update_time = None

@app.route("/")
def root():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email == "admin@govt.in" and password == "admin123":
            session["login"] = True
            return redirect("/dashboard")

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
    global latest_data, last_update_time
    latest_data = request.json
    last_update_time = datetime.now()
    return jsonify({"message": "ok"})

@app.route("/api/data")
def data():
    if not latest_data or not last_update_time:
        return jsonify({"connected": False})

    # if ESP silent > 10 sec → disconnected
    if (datetime.now() - last_update_time).seconds > 10:
        return jsonify({"connected": False})

    return jsonify({
        "connected": True,
        "total_bins": latest_data.get("total_bins", 0),
        "data": latest_data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
