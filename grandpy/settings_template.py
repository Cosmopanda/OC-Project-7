#!/usr/bin/python3

DEBUG = False
CSRF_ENABLED = True

GMAPS_URL = (
    "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
)
GMAPS_KEY = "YOUR_GOOGLE_API_KEY"
# https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Openclassroom&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=YOUR_GOOGLE_API_KEY

WIKI_URL = "https://fr.wikipedia.org/w/api.php?action=query&"
# https://fr.wikipedia.org/w/api.php?action=query&list=geosearch&gscoord=48.8747265|2.3505517&gsradius=1000&gslimit=10&format=json
# https://fr.wikipedia.org/w/api.php?action=query&pageids=5091748&prop=extracts&exintro&format=json&prop=info|extracts&inprop=url
