#!/usr/bin/python3
#                 __                              .__       .__    .__
#  ________ _____/  |_  ________ __  _____   ____ |__| _____|  |__ |__|
#  \___   // __ \   __\/  ___/  |  \/     \_/ __ \|  |/  ___/  |  \|  |
#   /    /\  ___/|  |  \___ \|  |  /  Y Y  \  ___/|  |\___ \|   Y  \  |
#  /_____ \\___  >__| /____  >____/|__|_|  /\___  >__/____  >___|  /__|
#        \/    \/          \/            \/     \/        \/     \/
# Made on patorjk.com

import os
import json

import requests

from .models import Place

GMAPS_URL = (
    "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
)
GMAPS_KEY = os.environ["GMAPS_KEY"]


class GMapsAPI:
    """GMaps API class
    Instance of this class can call endpoints on GMaps API
    To use this API, you need to put your Google API's key in your environment
    If you are on Linux, type the following in your terminal:
    export GMAPS_KEY=MY_API_KEY
    """

    def __init__(self):
        super(GMapsAPI, self).__init__()

    def place(self, search_term):
        """Place endpoint
        Args:
            search_term: string
        Returns:
            name
            geometry
            formatted_address
        """
        query = f"input={search_term}&inputtype=textquery&fields=formatted_address,name,geometry"
        try:
            response = requests.get(f"{GMAPS_URL}{query}&key={GMAPS_KEY}")
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
