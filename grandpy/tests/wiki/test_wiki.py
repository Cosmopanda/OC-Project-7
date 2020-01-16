#!/usr/bin/python3
import json
from unittest import TestCase
from apps.api.wiki import Wiki, WikiAPI, Type


class WikiTestCase(TestCase):
    def setUp(self):
        self.API = WikiAPI("Hôtel Bourrienne")
        self.page_query = self.API.build(Type.PAGE)
        self.geo_query = self.API.build(Type.GEO)
        self.geo_search = self.API.geo_search()
        self.page_search = self.API.page_search()
        self.page = self.API.page()

    def test_page(self):
        page = Wiki(
            page_id=5091748,
            title="Hôtel Bourrienne",
            extract='<p>L\'<b>Hôtel Bourrienne</b> (appelé aussi <b>Hôtel de Bourrienne</b> et <b>Petit Hôtel Bourrienne</b>) est un hôtel particulier du <abbr class="abbr" title="18ᵉ siècle"><span>XVIII</span><sup style="font-size:72%">e</sup></abbr> siècle situé au 58 rue d\'Hauteville dans le <abbr class="abbr" title="Dixième">10<sup>e</sup></abbr> arrondissement de Paris. Propriété privée, il est classé au titre des monuments historiques depuis le <time class="nowrap date-lien" datetime="1927-06-20" data-sort-value="1927-06-20">20 juin 1927</time>. En juillet 2015, il est acheté par l\'entrepreneur Charles Beigbeder pour en faire le siège de ses activités d\'investissement.</p>',
            url="https://fr.wikipedia.org/wiki/H%C3%B4tel_Bourrienne",
        )
        self.assertEqual(self.page, page)

    def test_geo_search(self):
        with open("../../data/geosearch.json") as f:
            data = json.load(f)
            self.assertEqual(self.geo_search, data)

    def test_page_search(self):
        with open("../../data/wikipage.json") as f:
            data = json.load(f)
            self.assertEqual(self.page_search, data)

    def test_build_page(self):
        page_query = "pageids=5091748&prop=extracts&exintro&format=json&prop=info|extracts&inprop=url"
        self.assertEqual(self.page_query, page_query)

    def test_build_geo(self):
        geo_query = "list=geosearch&gscoord=48.8747265|2.3505517&gsradius=1000&gslimit=10&format=json"
        self.assertEqual(self.geo_query, geo_query)
