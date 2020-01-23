#!/usr/bin/python3

from flask import Flask, render_template, jsonify
from .apps.query.query import Query

app = Flask(__name__)


@app.route("/")
def index():
    q = Query()
    q.tokenize_sentences()
    q.question()
    q.tagger()
    return render_template("index.html", query=q)


@app.route("/query/<string:query>", methods=["POST"])
def query():
    return jsonify({})


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
