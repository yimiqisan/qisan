#!/usr/bin/env python
# encoding: utf-8
"""
runserver.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from words import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)