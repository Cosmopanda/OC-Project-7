#!/usr/bin/python3
import json
from unittest import TestCase
from grandpy.apps.wiki.wiki import Wiki, WikiAPI
from grandpy.apps.gmaps.gmaps import Place


class WikiTestCase(TestCase):
    def setUp(self):
        self.API = WikiAPI()
        self.page_query = "pageids=5091748&prop=extracts&exintro&format=json&prop=info|extracts&inprop=url"
        self.geo_query = "list=geosearch&gscoord=48.8748465|2.3504873&gsradius=10000&gslimit=10&format=json"

        with open("data/wikipage.json") as f:
            self.page_search = json.load(f)

        with open("data/geosearch.json") as f:
            self.geo_search = json.load(f)

        self.place = Place(
            address="7 Cité Paradis, 75010 Paris, France",
            latitude=48.8748465,
            longitude=2.3504873,
            name="OpenClassrooms",
        )
        self.page = Wiki(
            page_id=5091748,
            title="Hôtel Bourrienne",
            extract='<p>L\'<b>Hôtel Bourrienne</b> (appelé aussi <b>Hôtel de Bourrienne</b> et <b>Petit Hôtel Bourrienne</b>) est un hôtel particulier du <abbr class="abbr" title="18ᵉ siècle"><span>XVIII</span><sup style="font-size:72%">e</sup></abbr> siècle situé au 58 rue d\'Hauteville dans le <abbr class="abbr" title="Dixième">10<sup>e</sup></abbr> arrondissement de Paris. Propriété privée, il est classé au titre des monuments historiques depuis le <time class="nowrap date-lien" datetime="1927-06-20" data-sort-value="1927-06-20">20 juin 1927</time>. En <time class="nowrap" datetime="2015-07" data-sort-value="2015-07">juillet 2015</time>, il est acheté par l\'entrepreneur Charles Beigbeder pour en faire le siège de ses activités d\'investissement.</p>',
            url="https://fr.wikipedia.org/wiki/H%C3%B4tel_Bourrienne",
        )

    def test_page(self):
        page = self.API.page(self.page_search)
        self.assertEqual(page.page_id, self.page.page_id)
        self.assertEqual(page.title, self.page.title)
        self.assertEqual(page.url, self.page.url)
        self.assertEqual(page.extract, self.page.extract)

    def test_geo_search(self):
        self.assertEqual(self.API.geo_search(self.geo_query), self.geo_search)

    def test_page_search(self):
        self.assertEqual(
            self.API.page_search(self.page_query, self.page_search), self.page_search
        )

    def test_build_page(self):
        self.assertEqual(self.API.build_page(self.page_search), self.page_query)

    def test_build_geo(self):
        self.assertEqual(self.API.build_geo(self.place), self.geo_query)
