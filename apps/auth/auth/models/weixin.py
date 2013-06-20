#!/usr/bin/env python
# encoding: utf-8


import sqlalchemy as sa
from words.database import ModelBase


class WeixinMappingModel(ModelBase):
    __tablename__ = 'weixin_mapping'

    ukey = sa.Column('ukey', sa.CHAR(6), sa.ForeignKey('account.ukey'),
                     nullable=False, primary_key=True, unique=True)
    username = sa.Column('username', sa.String(256), nullable=False,
                      primary_key=True, unique=True)
    date_created = sa.Column('date_created', sa.DateTime(timezone=True),
                             server_default=sa.func.current_timestamp(),
                             nullable=False, index=True)


#class WeixinMsgModel(ModelBase):
#    __tablename__ = 'weixin_msg'
#
#    id = sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
#    to_user_name = sa.Column('to_user_name', sa.Unicode(256), nullable=False, index=True)
#    from_user_name = sa.Column('from_user_name', sa.Unicode(256), nullable=False, index=True)
#    msg_type = sa.Column('msg_type', \
#        sa.Enum('text', 'image', 'location', 'url', 'event', 'music', 'news', name='msg_type'), \
#        nullable=True, index=True)
#    msg_id = sa.Column('msg_id', sa.Integer(), nullable=False)
#    content = sa.Column('content', sa.Unicode(1024), default='', server_default='', nullable=False)
#    date_created = = sa.Column('date_created', sa.DateTime(timezone=True),
#                            server_default=sa.func.current_timestamp(),
#                            nullable=False, index=True)
#
