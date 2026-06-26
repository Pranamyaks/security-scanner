from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Scan feature
@app.route("/scan", methods=["GET", "POST"])
def scan():
    if request.method == "POST":
        target = request.form["target"]
        return f"Scanning started for: {target} 🔍"
    
    return render_template("index.html")

# Login feature
@app.route("/login")
def login():
    return "Login Page 🔐"

# Run app
if __name__ == "__main__":
    app.run(debug=True)