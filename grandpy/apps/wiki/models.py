#!/usr/bin/python3


class Page:
    """docstring for Page."""

    def __init__(self, data):
        super(Page, self).__init__()
        self.page_id = data["pageid"]
        self.title = data["title"]
        self.extract = data["extract"]
        self.url = data["fullurl"]
