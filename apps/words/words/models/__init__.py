#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sqlalchemy as sa
from words.database import ModelBase

class Word(ModelBase):
    __tablename__ = 'word'
    id = sa.Column(sa.Integer, primary_key=True)
    word = sa.Column(sa.String(50), index=True)
    meaning = sa.Column(sa.String(1024))
    created = sa.Column(sa.DateTime(timezone=True), server_default=sa.func.current_timestamp()),

    def __init__(self, word=None, meaning=None):
        self.word = word
        self.meaning = meaning

    def __repr__(self):
        return '<Word %r>' % (self.word)