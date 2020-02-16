#!/usr/bin/python3
import os

import spacy
from boto.s3.connection import S3Connection

DEBUG = False
CSRF_ENABLED = True

GMAPS_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"

s3 = S3Connection(os.environ["GMAPS_KEY"])

WIKI_URL = "https://fr.wikipedia.org/w/api.php?action=query&"

STOPWORDS = "stopwords.json"

POS_TAGS = [
    "PROPN",  # Proper Noun
    "NOUN",
    "FAC",  # Buildings, airports, highways, bridges, etc.
    "ORG",  # Companies, agencies, institutions, etc.
    "GPE",  # Countries, cities, states.
    "LOC",  # Non-GPE locations, mountain ranges, bodies of water.
    "EVENT",  # Named hurricanes, battles, wars, sports events, etc.
]  # Move to constants.py/settings.py?

# French model https://spacy.io/models/fr/
NLP = spacy.load("fr_core_news_md")
