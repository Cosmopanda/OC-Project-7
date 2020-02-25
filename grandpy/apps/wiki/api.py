#!/usr/bin/python3
#                 __                              .__       .__    .__
#  ________ _____/  |_  ________ __  _____   ____ |__| _____|  |__ |__|
#  \___   // __ \   __\/  ___/  |  \/     \_/ __ \|  |/  ___/  |  \|  |
#   /    /\  ___/|  |  \___ \|  |  /  Y Y  \  ___/|  |\___ \|   Y  \  |
#  /_____ \\___  >__| /____  >____/|__|_|  /\___  >__/____  >___|  /__|
#        \/    \/          \/            \/     \/        \/     \/
# Made on patorjk.com

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
