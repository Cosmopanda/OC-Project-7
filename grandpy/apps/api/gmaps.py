#!/usr/bin/python3
import re
import json
import requests
from settings import GMAPS_URL, GMAPS_KEY


class Place:
    """docstring for Place."""

    def __init__(self, address, latitude, longitude, name, rating):
        super(Place, self).__init__()
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.rating = rating


class GMapsAPI:
    """docstring for GMapsAPI."""

    def __init__(self, query):
        super(GMapsAPI, self).__init__()
        self.query = query
        self.data = {}

    def build(self):
        return f"input={self.query}&inputtype=textquery&fields=formatted_address,name,rating,opening_hours,geometry"

    def place_search(self, query):
        try:
            response = requests.get(f"{GMAPS_URL}{query}&key={GMAPS_KEY}")
            return json.loads(response.content)["candidates"][0]
        except requests.exceptions.RequestException as e:
            print(e)

    def place(self, data):
        place = Place(
            address=data["formatted_address"],
            latitude=data["geometry"]["location"]["lat"],
            longitude=data["geometry"]["location"]["lng"],
            name=data["name"],
            rating=data["rating"],
        )
        return place
