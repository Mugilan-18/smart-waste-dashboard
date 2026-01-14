from flask import Flask, render_template, request, redirect, session, jsonify

app = Flask(__name__)
app.secret_key = "smart_waste_secret_key"

# LOGIN CREDENTIALS (DEMO)
USERNAME = "admin@govt.in"
PASSWORD = "1234"

# EMPTY STORAGE (NO ESP = NO BIN)
bin_data = {}   # key = bin_id, value = data

# ---------------- HOME ----------------
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"].strip()
        password = request.form["password"].strip()

        if email == USERNAME and password == PASSWORD:
            session["user"] = email
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", data=bin_data)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# ---------------- ESP DATA API ----------------
@app.route("/update", methods=["POST"])
def update():
    data = request.form

    bin_id = data.get("bin_id")
    area = data.get("area")
    gas = int(data.get("gas"))
    level = int(data.get("level"))

    status = "NORMAL"
    if gas > 400 or level > 80:
        status = "CRITICAL"

    bin_data[bin_id] = {
        "area": area,
        "gas": gas,
        "level": level,
        "status": status
    }

    return jsonify({"message": "Data received successfully"})

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)
