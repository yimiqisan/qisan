#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from flask import Flask
from views import blueprint_site, blueprint_apis, blueprint_weixin

app = Flask(__name__)
app.register_blueprint(blueprint_site)
app.register_blueprint(blueprint_apis)
app.register_blueprint(blueprint_weixin)