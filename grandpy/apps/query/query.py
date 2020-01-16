#!/usr/bin/python3
import re
import json
from unidecode import unidecode


class Query:
    """docstring for Query."""

    def __init__(self, query):
        super(Query, self).__init__()
        self.query = query
        self.parse()

    def parse(self):
        # Lowercase
        self.query = self.query.lower()

        # Regexep question

        # Clean
        self.query = unidecode(self.query)
        self.query = re.sub("(['-])", " ", self.query)

        # Stop words
        with open("../../stopwords.json") as f:
            stop_words = json.load(f)["stopwords"]
            stop_words = "|".join(stop_words)
            self.query = re.sub(stop_words, "", self.query)
