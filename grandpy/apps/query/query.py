#!/usr/bin/python3
import re
import json
from unidecode import unidecode
from grandpy.settings import STOPWORDS, POS_TAGS, NLP


class Query:
    """docstring for Query."""

    def __init__(self, query):
        super(Query, self).__init__()
        self.query = query

    def find_question(self, sentences):
        for sentence in sentences:
            if sentence[-1] == "?":
                return sentence

    def tokenize_sentences(self):
        """Returns a list of sentences"""
        return [sentence.text for sentence in NLP(self.query).sents]

    def pipe(self):
        tokens = []

        sentences = self.tokenize_sentences()
        question = self.find_question(sentences)

        # Tokenizes the words and recognizes entities
        for doc in NLP.pipe([question]):
            for entity in doc.ents:
                tokens.append(entity.text)

        return " ".join(tokens)

    def parse(self):
        tokens = []

        sentences = self.tokenize_sentences()
        question = self.find_question(sentences)

        # Tokenizes and tags words
        tagged = [(token, token.pos_) for token in NLP(question)]

        # Looks for relevant words not matching stop words
        with open(STOPWORDS) as f:
            stopwords = json.load(f)["stopwords"]
            for token in tagged:
                token_str = str(token[0])
                if token[1] in POS_TAGS and token_str not in stopwords:
                    tokens.append(token_str)

        return " ".join(tokens)
