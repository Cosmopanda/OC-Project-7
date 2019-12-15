# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "message"


if __name__ == "__main__":
    app.run(threaded=True, port=1337)
