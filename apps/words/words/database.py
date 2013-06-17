#!/usr/bin/env python
# encoding: utf-8
"""
database.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://words:wwww@localhost/words', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
ModelBase = declarative_base()
ModelBase.query = db_session.query_property()

def init_db():
    import words.models
    ModelBase.metadata.create_all(bind=engine)