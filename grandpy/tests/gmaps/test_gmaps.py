#!/usr/bin/python3
import json
from unittest import TestCase
from apps.api.gmaps import Place, GMapsAPI


class GMapsTestCase(TestCase):
    def setUp(self):
        self.API = GMapsAPI("connais adresse OpenClassrooms")
        self.place_query = GMapsAPI.build()
        self.place_search = GMapsAPI.place_search()
        self.place = GMapsAPI.place()

    def test_place_search(self):
        with open("../../data/places.json") as f:
            data = json.load(f)
            self.assertEqual(self.place, data)

    def test_build(self):
        place_query = "input=Openclassroom&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry"
        self.assertEqual(self.place_query, place_query)

    def test_place(self):
        place = Place(
            address="7 Cité Paradis, 75010 Paris, France",
            latitude=48.8748465,
            longitude=2.3504873,
            name="OpenClassrooms",
            rating=3.3,
        )
        self.assertEqual(self.place, place)
