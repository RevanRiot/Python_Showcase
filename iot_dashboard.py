# File: iot_dashboard.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    data = {
        "temperature": 25.5,
        "humidity": 60,
        "status": "Active"
    }
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
