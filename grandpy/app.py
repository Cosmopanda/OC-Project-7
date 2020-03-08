#!/usr/bin/python3

import os
import json

import nltk
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

from constants import MESSAGES
from apps.query.forms import QueryForm
from apps.query.query import Query
from apps.gmaps.api import GMapsAPI
from apps.gmaps.models import Place
from apps.wiki.api import WikiAPI
from apps.wiki.models import Page

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": "*"}})
app.config.from_pyfile("settings.py")

nltk.download("punkt")

GMAPS_KEY = os.environ["GMAPS_KEY"]


def format_answer(place=None, page=None, search_term=True):
    answer = {}

    if not search_term:
        answer["error"] = MESSAGES["no_question"]
        return answer
    if not place:
        answer["error"] = MESSAGES["not_found"]
        return answer
    if place:
        answer[
            "address"
        ] = f"Voici l'addresse pour {place.name}: {place.address}. "
        if not page:
            answer["error"] = MESSAGES["no_wiki_result"]
        else:
            answer["random"] = MESSAGES["random"][0]
            answer[
                "wiki"
            ] = f"{page.extract[33:].replace('<p>', '').replace('</p>', '') }<br/>"
            answer[
                "link"
            ] = "Tu peux trouver plus d'informations ici <a href='{page.url}'>Wikipedia</a>"
    answer[
        "map"
    ] = f"""
        <iframe
          width="400"
          height="400"
          frameborder="0" style="border:0"
          src="https://www.google.com/maps/embed/v1/view?key={GMAPS_KEY}
          &center={place.latitude},{place.longitude}
          &zoom=18" allowfullscreen>
        </iframe>
        """
    return answer


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
                search_term = parser.parse()
                if not search_term:
                    answer = format_answer(search_term=False)
                    return jsonify(query=query, answer=answer)
                gmaps = GMapsAPI()
                response = gmaps.place(search_term)
                if response["status"] == "ZERO_RESULTS":
                    answer = format_answer(search_term=False)
                    return jsonify(query=query, answer=answer)
                place = Place(response["candidates"][0])
                if not place:
                    answer = format_answer()
                    return jsonify(query=query, answer=answer)
                wiki = WikiAPI()
                geo_search = wiki.geo(place)["query"]["geosearch"][0]
                response = wiki.page(geo_search)["query"]["pages"][
                    str(geo_search["pageid"])
                ]
                page = Page(response)
                if not page:
                    answer = format_answer(place=place)
                    return jsonify(query=query, answer=answer)
                answer = format_answer(place, page)
                return jsonify(query=query, answer=answer)
        except Exception as e:
            print(e)
            return jsonify(query=query, answer="Je n'ai pas bien entendu.")


if __name__ == "__main__":
    app.run(threaded=True, debug=False)
