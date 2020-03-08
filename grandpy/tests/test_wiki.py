#!/usr/bin/python3

import json
from unittest import TestCase

from ..apps.wiki.api import WikiAPI
from ..apps.wiki.models import Page
from ..apps.gmaps.models import Place


class WikiTestCase(TestCase):
    def setUp(self):
        self.API = WikiAPI()
        with open("mocks/places.json") as f:
            data = json.load(f)
            self.place = Place(data)
        with open("mocks/wikipage.json") as f:
            data = json.load(f)
            self.page = Page(data["query"]["pages"]["5091748"])
        self.geo_results = self.API.geo(self.place)["query"]["geosearch"]
        self.page_results = self.API.page(self.geo_results[0])["query"][
            "pages"
        ]

    def test_geo(self):
        self.assertTrue(self.geo_results)
        response = self.geo_results[0]
        self.assertTrue(isinstance(response["pageid"], int))
        self.assertTrue(isinstance(response["title"], str))
        self.assertTrue(isinstance(response["lat"], float))
        self.assertTrue(isinstance(response["lon"], float))

    def test_page(self):
        self.assertTrue(self.page_results)
        response = self.page_results[str(self.geo_results[0]["pageid"])]
        self.assertTrue(isinstance(response["title"], str))
        self.assertTrue(isinstance(response["fullurl"], str))
        self.assertTrue(isinstance(response["extract"], str))

    def test_create_page(self):
        page = Page(self.page_results[str(self.geo_results[0]["pageid"])])
        self.assertEqual(page.page_id, self.page.page_id)
        self.assertEqual(page.title, self.page.title)
        self.assertEqual(page.url, self.page.url)
