#!/usr/bin/python3
import re
import json
import spacy
from spacy.lang.fr import French
from unidecode import unidecode


NLP = spacy.load("fr_core_news_md")  # Move to constants.py/settings.py?
POS_TAGS = [
    "PROPN",  # Proper Noun
    "NOUN",
    "FAC",  # Buildings, airports, highways, bridges, etc.
    "ORG",  # Companies, agencies, institutions, etc.
    "GPE",  # Countries, cities, states.
    "LOC",  # Non-GPE locations, mountain ranges, bodies of water.
    "EVENT",  # Named hurricanes, battles, wars, sports events, etc.
]  # Move to constants.py/settings.py?


class Query:
    """docstring for Query."""

    def __init__(self):
        super(Query, self).__init__()
        self.query = (
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        )

    def run(self):
        self.tokenize_sentences()
        self.question()
        self.tagger()

    # Remove?
    def clean(self):
        self.query = re.sub("(['-])", " ", self.query)

    def parse(self):
        parsed = []
        for token in self.query:
            if token[1] in POS_TAGS:
                parsed.append(token)
        self.query = parsed

    def tokenize_sentences(self):
        doc = NLP(self.query)
        self.query = [sentence.text for sentence in doc.sents]

    def question(self):
        q = []
        for sentence in self.query:
            if sentence[-1] == "?":
                q.append(sentence)
        self.query = q[0]

    def tagger(self):
        doc = NLP(self.query)
        self.query = [(token, token.pos_) for token in doc]
