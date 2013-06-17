#!/usr/bin/env python
# encoding: utf-8
"""
form.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from flask.ext.wtf import Form, validators, fields


class WeixinConnectForm(Form):
    signature = fields.StringField(validators=[validators.Required()])
    timestamp = fields.StringField(validators=[validators.Required()])
    nonce = fields.StringField(validators=[validators.Required()])
    echostr = fields.StringField(validators=[validators.Required()])
