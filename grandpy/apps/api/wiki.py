#!/usr/bin/python3
import json
import requests
from enum import Enum
from settings import WIKI_URL


class Type(Enum):
    PAGE = 1
    GEO = 2


class Wiki:
    """docstring for Wiki."""

    def __init__(self, page_id, title, extract, link):
        super(Wiki, self).__init__()
        self.page_id = page_id
        self.title = title
        self.extract = extract
        self.url = link


class WikiAPI:
    """docstring for WikiAPI."""

    def __init__(self, data):
        super(WikiAPI, self).__init__()
        self.data = data
        self.geo_query = ""
        self.page_query = ""

    def run(self):
        self.build()
        self.geo_search()
        self.page_search()
        return self.page()

    def build(self, type):
        if type == Type.GEO:
            self.geo_query = (
                f"list=geosearch&gscoord={self.data.latitude}|"
                f"{self.data.longitude}&gsradius=10000&gslimit=10&format=json"
            )
        else:
            self.page_query = (
                f"pageids={self.data.page_id}&prop=extracts&exintro&"
                "format=json&prop=info|extracts&inprop=url"
            )

    def geo_search(self):
        try:
            response = requests.get(f"{WIKI_URL}{self.geo_query}")
            self.data = json.loads(response.content)["query"]["geosearch"][0]
        except requests.exceptions.RequestException as e:
            print(e)

    def page_search(self):
        try:
            response = requests.get(f"{WIKI_URL}{self.page_query}")
            self.data = json.loads(response.content)["query"]["pages"][
                str(self.data.page_id)
            ]
        except requests.exceptions.RequestException as e:
            print(e)

    def page(self):
        wiki = Wiki(
            address=self.data["formatted_address"],
            latitude=self.data["geometry"]["location"]["lat"],
            longitude=self.data["geometry"]["location"]["lng"],
            name=self.data["name"],
            rating=self.data["rating"],
        )
        return wiki
