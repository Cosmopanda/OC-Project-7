#!/usr/bin/python3
import unittest
from apps.query.query import Query


class QueryTestCase(unittest.TestCase):
    def setUp(self):
        self.query = Query(
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        )
        self.query_sentences = [
            "Salut GrandPy !",
            "Est-ce que tu connais l'adresse d'OpenClassrooms ?",
        ]
        self.query_question = (
            "Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        )
        self.search_term = "OpenClassrooms"

    def test_tokenize_sentences(self):
        self.assertEqual(self.query.tokenize_sentences(), self.query_sentences)

    def test_find_question(self):
        self.assertEqual(
            self.query.find_question(self.query_sentences), self.query_question
        )

    def test_parse(self):
        self.assertEqual(self.query.parse(), self.search_term)

    def test_pipe(self):
        self.assertEqual(self.query.pipe(), self.search_term)
