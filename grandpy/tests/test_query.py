#!/usr/bin/python3

import unittest
from grandpy.apps.query.query import Query


class QueryTestCase(unittest.TestCase):
    def setUp(self):
        self.query = Query(
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        )
        self.search_term = "OpenClassrooms"

    def test_parse(self):
        self.assertEqual(self.query.parse(), self.search_term)
