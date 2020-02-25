#!/usr/bin/python3
#                 __                              .__       .__    .__
#  ________ _____/  |_  ________ __  _____   ____ |__| _____|  |__ |__|
#  \___   // __ \   __\/  ___/  |  \/     \_/ __ \|  |/  ___/  |  \|  |
#   /    /\  ___/|  |  \___ \|  |  /  Y Y  \  ___/|  |\___ \|   Y  \  |
#  /_____ \\___  >__| /____  >____/|__|_|  /\___  >__/____  >___|  /__|
#        \/    \/          \/            \/     \/        \/     \/
# Made on patorjk.com

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
