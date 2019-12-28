#!/usr/bin/python3


class Place:
    """docstring for Place."""

    def __init__(self, address, latitude, longitude, name, rating):
        super(Place, self).__init__()
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        self.rating = rating


class GMapsAPI:
    """docstring for GMapsAPI."""

    def __init__(self):
        super(GMapsAPI, self).__init__()
