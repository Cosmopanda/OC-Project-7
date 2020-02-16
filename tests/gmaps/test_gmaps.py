#!/usr/bin/python3
import json
from unittest import TestCase
from grandpy.apps.api.gmaps import Place, GMapsAPI


class GMapsTestCase(TestCase):
    def setUp(self):
        self.API = GMapsAPI("OpenClassrooms")
        self.place_query = "input=OpenClassrooms&inputtype=textquery&fields=formatted_address,name,opening_hours,geometry"
        with open("data/places.json") as f:
            self.place_search = json.load(f)
        self.place = Place(
            address="7 Cité Paradis, 75010 Paris, France",
            latitude=48.8748465,
            longitude=2.3504873,
            name="OpenClassrooms",
        )

    def test_place_search(self):
        self.assertEqual(self.API.place_search(self.place_query), self.place_search)

    def test_build(self):
        self.assertEqual(self.API.build(), self.place_query)

    def test_place(self):
        place = self.API.place(self.place_search)
        self.assertEqual(place.address, self.place.address)
        self.assertEqual(place.latitude, self.place.latitude)
        self.assertEqual(place.longitude, self.place.longitude)
        self.assertEqual(place.name, self.place.name)
