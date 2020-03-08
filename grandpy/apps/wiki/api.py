#!/usr/bin/python3

import json

import requests

WIKI_URL = "https://fr.wikipedia.org/w/api.php?action=query&"


class WikiAPI:
    """docstring for WikiAPI."""

    def __init__(self):
        super(WikiAPI, self).__init__()

    def geo(self, place):
        query = (
            f"list=geosearch&gscoord={place.latitude}|{place.longitude}"
            f"&gsradius=10000&gslimit=10&format=json"
        )
        try:
            response = requests.get(f"{WIKI_URL}{query}")
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(e)

    def page(self, page):
        query = (
            f"pageids={page['pageid']}&prop=extracts&exintro&"
            "format=json&prop=info|extracts&inprop=url"
        )
        try:
            response = requests.get(f"{WIKI_URL}{query}")
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
