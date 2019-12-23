#!/usr/bin/python3


class Query:
    """docstring for Query."""

    def __init__(self, query):
        super(Query, self).__init__()
        self.query = query
        self.parse()
        self.query_dict = self.to_dict()

    def parse(self):
        pass

    def to_dict(self):
        pass
