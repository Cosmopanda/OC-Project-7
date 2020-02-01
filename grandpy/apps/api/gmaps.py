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

    def run(self):
        self.build()
        self.place_search()
        return self.place()

    def build(self):
        self.query = (
            f"input={self.query}&inputtype=textquery&fields=photos,"
            "formatted_address,name,rating,opening_hours,geometry"
        )

    def place_search(self):
        try:
            response = requests.get(f"{GMAPS_URL}{self.query}&key={GMAPS_KEY}")
            self.data = json.loads(response.content)["candidates"][0]
        except requests.exceptions.RequestException as e:
            print(e)

    def place(self):
        place = Place(
            address=self.data["formatted_address"],
            latitude=self.data["geometry"]["location"]["lat"],
            longitude=self.data["geometry"]["location"]["lng"],
            name=self.data["name"],
            rating=self.data["rating"],
        )
        return place
