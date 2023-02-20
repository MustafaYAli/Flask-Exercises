from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    now = datetime.now()
    current_time = now.strftime("%A, %Y-%m-%d %H:%M:%S")
    return f"<h1>The current day and time is {current_time}</h1>"


if __name__ == "__main__":
    app.run()














