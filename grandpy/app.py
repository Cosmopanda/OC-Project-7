#!/usr/bin/python3
#                 __                              .__       .__    .__
#  ________ _____/  |_  ________ __  _____   ____ |__| _____|  |__ |__|
#  \___   // __ \   __\/  ___/  |  \/     \_/ __ \|  |/  ___/  |  \|  |
#   /    /\  ___/|  |  \___ \|  |  /  Y Y  \  ___/|  |\___ \|   Y  \  |
#  /_____ \\___  >__| /____  >____/|__|_|  /\___  >__/____  >___|  /__|
#        \/    \/          \/            \/     \/        \/     \/
# Made on patorjk.com

import os
import json

import nltk
from flask_cors import CORS
from flask import Flask, render_template, jsonify, request

from .constants import MESSAGES
from .apps.query.forms import QueryForm
from .apps.query.query import Query
from .apps.gmaps.api import GMapsAPI
from .apps.gmaps.models import Place
from .apps.wiki.api import WikiAPI
from .apps.wiki.models import Page

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": "*"}})
app.config.from_pyfile("settings.py")

nltk.download("punkt")

GMAPS_KEY = os.environ["GMAPS_KEY"]


def format_answer(place=None, page=None):
    answer = ""

    if not place:
        answer += MESSAGES["not_found"]
        return answer
    if place:
        if not page:
            answer += MESSAGES["no_wiki_result"]
            answer += f"Voici l'addresse pour {place.name}: {place.address}. "
            answer += f"""
            <iframe
              width="400"
              height="400"
              frameborder="0" style="border:0"
              src="https://www.google.com/maps/embed/v1/view?key={GMAPS_KEY}
              &center={place.latitude},{place.longitude}
              &zoom=17" allowfullscreen>
            </iframe>
            """
        else:
            answer += f"Voici l'addresse pour {place.name}: {place.address}. "
            answer += MESSAGES["random"][0]
            answer += f"{page.extract} Tu peux trouver plus d'informations ici <a href='{page.url}'>Wikipedia</a><br/>"
            answer += f"""
            <iframe
              width="400"
              height="400"
              frameborder="0" style="border:0"
              src="https://www.google.com/maps/embed/v1/view?key={GMAPS_KEY}
              &center={place.latitude},{place.longitude}
              &zoom=17" allowfullscreen>
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
                gmaps = GMapsAPI()
                response = gmaps.place(search_term)["candidates"][0]
                place = Place(response)
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
            return jsonify(query=query, answer="Je n'ai pas compris")
    return jsonify(query=query, answer="Je n'ai pas compris")


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
