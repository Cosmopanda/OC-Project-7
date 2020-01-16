#!/usr/bin/python3
import unittest
from apps.query.query import Query


class QueryTestCase(unittest.TextCase):
    def setUp(self):
        self.query = Query(
            "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        )

    def test_parse(self):
        self.assertEqual(self.query.query == "connais adresse OpenClassrooms")
