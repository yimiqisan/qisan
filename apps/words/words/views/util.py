#!/usr/bin/env python
# encoding: utf-8
"""
util.py

Created by 刘 智勇 on 2013-06-16.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""


from hashlib import sha1
from lxml import etree

_sha1 = lambda x: sha1(x).hexdigest()


def _check_signature(message):
    signature = message.pop('signature')
    keylist = list(message)
    keylist.sort()
    compare = ''.join([str(message[key]) for key in keylist])
    other_keylist = ['timestamp', 'nonce', 'token']
    other_compare = ''.join([str(message[key]) for key in other_keylist])
    return signature == _sha1(compare) or signature == _sha1(other_compare)


def check_xml_wf(xml):
    """ 使用lxml.etree.parse 检测xml是否符合语法规范"""
    # 参数xml是经过StringIO处理过的instance类型
    try:
        xml = etree.parse(xml)
        return xml
    except etree.XMLSyntaxError, e:
        return False

def get_message_data(xml):
    """解析xml 提取其中数据 并存入一个dict"""
    data_dict = {}

    for node in xml.iter():
        data_dict[node.tag] = node.text
    return data_dict

def prepare_reply_data(from_user_name, to_user_name, content):
    """准 备 消 息 需 要 返 回 数 据"""
    reply_dict = {}
    reply_dict['ToUserName'] = from_user_name
    reply_dict['FromUserName'] = to_user_name
    reply_dict['CreateTime'] = int(time())
    ask = WeixinRequest(from_user_name, to_user_name, content)
    replies = ask.get_replies()
    if not replies:
        # 当 搜 索 结 果 为 空 或 问 题 不 符 合 规 范 时 列 表 为 空
        return ''
    else:
        reply = reply_message(ask, reply_dict, replies)
        return reply




