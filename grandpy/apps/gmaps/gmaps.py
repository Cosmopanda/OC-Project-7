#!/usr/bin/python3
import os
import json

import requests

GMAPS_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
GMAPS_KEY = os.environ["GMAPS_KEY"]


class Place:
    """docstring for Place."""

    def __init__(self, address, latitude, longitude, name):
        super(Place, self).__init__()
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.name = name


class GMapsAPI:
    """docstring for GMapsAPI."""

    def __init__(self, query):
        super(GMapsAPI, self).__init__()
        self.query = query

    def run(self):
        query = self.build()
        data = self.place_search(query)
        if data:
            return self.place(data)
        return

    def build(self):
        return f"input={self.query}&inputtype=textquery&fields=formatted_address,name,geometry"

    def place_search(self, query):
        try:
            response = requests.get(f"{GMAPS_URL}{query}&key={GMAPS_KEY}")
            response = json.loads(response.content)
            if response["candidates"]:
                return response["candidates"][0]
            else:
                return
        except requests.exceptions.RequestException as e:
            print(e)

    def place(self, data):
        place = Place(
            address=data["formatted_address"],
            latitude=data["geometry"]["location"]["lat"],
            longitude=data["geometry"]["location"]["lng"],
            name=data["name"],
        )
        return place
