#!/usr/bin/env python
# encoding: utf-8
"""
weixin.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from time import time
from StringIO import StringIO

from flask import request, current_app as app, abort
from flask import Blueprint

from words.database import init_db, db_session as db
from words.models import Word

from util import _check_signature, check_xml_wf, get_message_data
from forms import WeixinConnectForm


blueprint_weixin = Blueprint('blueprint_weixin', __name__, url_prefix='/wx')
token = 'b61e7ad8c5194994903cd11be6160dc0'


TEXT_TPL = '''
    <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName> 
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        <FuncFlag>0</FuncFlag>
    </xml>
'''

@blueprint_weixin.route('/', methods=['GET'])
def get():
    get_params = WeixinConnectForm(request.args, csrf_enabled=False)
    if not get_params.validate():
        abort(404)
    message = get_params.data
    echostr = message.pop('echostr')
    message['token'] = token
    if not _check_signature(message):
        abort(404)
    return echostr

def query_word(word):
    w = Word.query.filter(Word.word==word).first()
    return w.meaning.encode('utf8')

@blueprint_weixin.route('/', methods=['POST'])
def post():
    postStr = request.data
    xml = StringIO(postStr)
    check_xml = check_xml_wf(xml)
    if not check_xml:
        return False
    message_dict = get_message_data(check_xml)
    try:
        to_user_name = message_dict['ToUserName']
        from_user_name = message_dict['FromUserName']
        content = message_dict.get('Content', '').strip()
        event = message_dict.get('Event', '').strip()
        event_key = message_dict.get('EventKey', '').strip()
        message_type = message_dict['MsgType']
    except KeyError, e:
        return result
    
    reply_dict = {}
    reply_dict['ToUserName'] = from_user_name
    reply_dict['FromUserName'] = to_user_name
    reply_dict['CreateTime'] = int(time())

    if message_type == 'text':
        reply_dict['Content'] = query_word(content)
        result = TEXT_TPL.format(**reply_dict)
    else:
        reply_dict['Content'] = 'error'
    return result

