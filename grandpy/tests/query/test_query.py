#!/usr/bin/python3
import unittest
from apps.query.query import Query


class QueryTestCase(unittest.TestCase):
    def setUp(self):
        self.query = Query(
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        )
        self.tokenized = [
            "Salut GrandPy !",
            "Est-ce que tu connais l'adresse d'OpenClassrooms ?",
        ]
        self.question = "Est-ce que tu connais l'adresse d'OpenClassrooms ?"

    def test_tokenize_sentences(self):
        self.assertEqual(self.query.tokenize_sentences() == self.tokenized)

    def test_question(self):
        self.assertEqual(self.query.question() == self.question)

    # Can't test the result. Maybe test isinstance(spacy.tokens.token.Token)?
    # def test_tagger(self):
    # self.assertEqual(self.query.tagger() == self.tagged)
