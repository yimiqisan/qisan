#!/usr/bin/env python
# encoding: utf-8
"""
apis.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from flask import request, current_app as app
from flask import Blueprint
from words.database import init_db, db_session as db
from words.models import Word

blueprint_apis = Blueprint('blueprint_apis', __name__, url_prefix='/apis/words/')


@blueprint_apis.route('retrieve/', methods=['GET'])
@blueprint_apis.route('retrieve/<string:word>/', methods=['GET'])
def retrieve(word=None):
    if word is None:
        w = Word.query.all()[-1]
    else:
        w = Word.query.filter(Word.word==word).first()
    return w.word +':'+ w.meaning
    
@blueprint_apis.route('create/', methods=['POST'])
def create():
    word = request.form['word']
    meaning = request.form['meaning']
    w = Word(word, meaning)
    try:
        db.add(w)
        db.commit()
    except Exception, e:
        return e
    return 'OK'