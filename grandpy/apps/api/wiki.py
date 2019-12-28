#!/usr/bin/python3


class Wiki:
    """docstring for Wiki."""

    def __init__(self, page_id, title, extract, link):
        super(Wiki, self).__init__()
        self.page_id = page_id
        self.title = title
        self.extract = extract
        self.link = link


class WikiAPI:
    """docstring for WikiAPI."""

    def __init__(self):
        super(WikiAPI, self).__init__()

    def geo_search(self):
        pass

    def page_search(self):
        pass
