#!/usr/bin/python3
import spacy

DEBUG = False
CSRF_ENABLED = True

GMAPS_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
# https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Openclassroom&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=YOUR_GOOGLE_API_KEY
GMAPS_KEY = "YOUR_API_KEY"

# https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=48.8747265|2.3505517&gsradius=1000&gslimit=10&format=json
# https://fr.wikipedia.org/w/api.php?action=query&pageids=5091748&prop=extracts&exintro&format=json&prop=info|extracts&inprop=url
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
