from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

latest_data = None

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if (
            request.form["email"] == "admin@govt.in"
            and request.form["password"] == "admin123"
        ):
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", data=latest_data)

@app.route("/api/update", methods=["POST"])
def update():
    global latest_data
    data = request.json

    # STATUS LOGIC
    if data["level"] > 80 or data["gas"] > 400:
        status = "CRITICAL"
    elif data["level"] > 60 or data["gas"] > 300:
        status = "WARNING"
    else:
        status = "NORMAL"

    data["status"] = status
    latest_data = data

    return jsonify({"message": "Data received"}), 200

if __name__ == "__main__":
    app.run()
