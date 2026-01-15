from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "smart-waste-secret"

# Dummy login (demo purpose)
USER_EMAIL = "admin@govt.in"
USER_PASSWORD = "admin123"

# ESP DATA (initially empty)
ESP_DATA = []

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == USER_EMAIL and password == USER_PASSWORD:
            session["user"] = email
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        data=ESP_DATA,
        total_bins=len(ESP_DATA)
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ESP will call this API later
@app.route("/api/esp-data", methods=["POST"])
def esp_data():
    global ESP_DATA
    ESP_DATA = [request.json]
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
