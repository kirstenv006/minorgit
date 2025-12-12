from flask import Flask

app = Flask(__name__)  # <- Dit is het object dat Gunicorn zoekt

@app.route("/")
def home():
    return "Hello, world!"
