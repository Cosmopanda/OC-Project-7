#!/usr/bin/python3
#                 __                              .__       .__    .__
#  ________ _____/  |_  ________ __  _____   ____ |__| _____|  |__ |__|
#  \___   // __ \   __\/  ___/  |  \/     \_/ __ \|  |/  ___/  |  \|  |
#   /    /\  ___/|  |  \___ \|  |  /  Y Y  \  ___/|  |\___ \|   Y  \  |
#  /_____ \\___  >__| /____  >____/|__|_|  /\___  >__/____  >___|  /__|
#        \/    \/          \/            \/     \/        \/     \/
# Made on patorjk.com

import json
from unittest import TestCase

from ..apps.gmaps.api import GMapsAPI
from ..apps.gmaps.models import Place


class GMapsTestCase(TestCase):
    def setUp(self):
        self.API = GMapsAPI()
        self.response = self.API.place("OpenClassrooms")
        with open("mocks/places.json") as f:
            data = json.load(f)
            self.place = Place(data)

    def test_place_search(self):
        self.assertEqual(self.response["status"], "OK")
        self.assertTrue(self.response["candidates"])
        response = self.response["candidates"][0]
        self.assertTrue(isinstance(response["formatted_address"], str))
        self.assertTrue(isinstance(response["geometry"], dict))
        self.assertTrue(isinstance(response["name"], str))

    def test_create_place(self):
        place = Place(self.response["candidates"][0])
        self.assertEqual(place.address, self.place.address)
        self.assertEqual(place.latitude, self.place.latitude)
        self.assertEqual(place.longitude, self.place.longitude)
        self.assertEqual(place.name, self.place.name)
