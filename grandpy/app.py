#!/usr/bin/python3
import json

from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

from apps.query.forms import QueryForm
from apps.query.query import Query
from apps.gmaps.gmaps import GMapsAPI
from apps.wiki.wiki import WikiAPI

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": "*"}})
app.config.from_pyfile("settings.py")


@app.route("/")
def index():
    query_form = QueryForm()
    return render_template("index.html", form=query_form)


@app.route("/query", methods=["POST"])
def query():
    if request.method == "POST":
        try:
            query = request.form["query"]
            if query:
                parser = Query(query)
                search_term = parser.pipe()
                if not search_term:
                    search_term = parser.parse()
                gmaps = GMapsAPI(search_term)
                place = gmaps.run()
                wiki = WikiAPI()
                page = wiki.run(place)
                return jsonify(
                    query=query,
                    place=json.dumps(place.__dict__),
                    page=json.dumps(page.__dict__),
                )
        except Exception as e:
            print(e)
            return jsonify(answer="Je n'ai pas compris")
    return jsonify(answer="Je n'ai pas compris")


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
