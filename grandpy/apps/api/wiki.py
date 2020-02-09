#!/usr/bin/python3
import json
import requests
from settings import WIKI_URL


class Wiki:
    """docstring for Wiki."""

    def __init__(self, page_id, title, extract, url):
        super(Wiki, self).__init__()
        self.page_id = page_id
        self.title = title
        self.extract = extract
        self.url = url


class WikiAPI:
    """docstring for WikiAPI."""

    def __init__(self):
        super(WikiAPI, self).__init__()

    def run(self, place):
        geo_query = self.build_geo(place)
        res = self.geo_search(geo_query)
        page_query = self.build_page(res)
        data = self.page_search(page_query, res)
        return self.page(data)

    def build_geo(self, place):
        return (
            f"list=geosearch&gscoord={place.latitude}|"
            f"{place.longitude}&gsradius=10000&gslimit=10&format=json"
        )

    def build_page(self, data):
        return (
            f"pageids={data['pageid']}&prop=extracts&exintro&"
            "format=json&prop=info|extracts&inprop=url"
        )

    def geo_search(self, geo_query):
        try:
            response = requests.get(f"{WIKI_URL}{geo_query}")
            data = json.loads(response.content)["query"]["geosearch"][0]
            return data

        except requests.exceptions.RequestException as e:
            print(e)

    def page_search(self, page_query, res):
        try:
            response = requests.get(f"{WIKI_URL}{page_query}")
            data = json.loads(response.content)["query"]["pages"][str(res["pageid"])]
            return data
        except requests.exceptions.RequestException as e:
            print(e)

    def page(self, data):
        wiki = Wiki(
            page_id=data["pageid"],
            title=data["title"],
            extract=data["extract"],
            url=data["fullurl"],
        )
        return wiki
