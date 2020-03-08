#!/usr/bin/python3

import re
import json

from unidecode import unidecode
from nltk import sent_tokenize, word_tokenize


class Query:
    """docstring for Query."""

    def __init__(self, query):
        super(Query, self).__init__()
        self.query = query

    def parse(self):
        tokens = []
        question = ""

        # Tokenize sentences
        sentences = sent_tokenize(self.query)

        # Find a question
        for sentence in sentences:
            if sentence[-1] == "?":
                question = [sentence]
                break

        # Removing non alpha-numeric characters
        question = re.sub(r"[\_\-\'\"]", " ", question[0][:-1])

        # Tokenizes and tags words
        tagged = word_tokenize(question)

        # Looks for relevant words not matching stop words
        with open("./stopwords.json") as f:
            stopwords = json.load(f)["stopwords"]
            for token in tagged:
                if token.lower() not in stopwords:
                    tokens.append(token)

        return " ".join(tokens)
