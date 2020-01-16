#!/usr/bin/python3
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

    def __init__(self, query):
        super(WikiAPI, self).__init__()
        self.query = query
        self.geo_query = ""
        self.page_query = ""

    def build(self, type):
        if isinstance(type, Type.GEO):
            self.geo_query = (
                f"list=geosearch&gscoord={self.query['latitude']}|"
                f"{self.query['longitude']}&gsradius=10000&gslimit=10&format=json"
            )
        else:
            self.page_query = (
                f"pageids={self.query}&prop=extracts&exintro&"
                "format=json&prop=info|extracts&inprop=url"
            )

    def geo_search(self):
        pass

    def page_search(self):
        pass

    def page(self):
        pass
