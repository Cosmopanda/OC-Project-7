#!/usr/bin/python3

from wtforms import Form, StringField, validators


class QueryForm(Form):
    query = StringField("Query", [validators.Length(min=3, max=255)])
