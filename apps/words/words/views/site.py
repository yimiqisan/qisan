#!/usr/bin/env python
# encoding: utf-8
"""
site.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from flask import current_app as app
from flask import Blueprint
from words.database import init_db, db_session as db
from words.models import Word

blueprint_site = Blueprint('blueprint_site', __name__, url_prefix='/words')

@blueprint_site.route('/init/')
def init():
    init_db()
    return 'OK'

@blueprint_site.route('/<string:word>/')
def index(word):
    w = Word.query.filter(Word.word==word).first()
    return w.word + w.meaning

@blueprint_site.route('/insert/')
def insert():
    w = Word('lzy', '刘智勇')
    try:
        db.add(w)
        db.commit()
    except Exception, e:
        return e
    return 'insert success'