#!/usr/bin/env python
# encoding: utf-8


import sqlalchemy as sa
from words.database import ModelBase


class AccountModel(ModelBase):
    __tablename__ = 'account'

    ukey = sa.Column('ukey', db.CHAR(6), nullable=False, primary_key=True)
    nickname = sa.Column('nickname', sa.Unicode(256), nullable=False, unique=True)
    gender = sa.Column('gender', sa.Enum('male', 'female', name='user_gender'), nullable=True)
    avatar = sa.Column('avatar', "db.HashkeyType()", nullable=True)
    date_created = = sa.Column('date_created', sa.DateTime(timezone=True),
                            server_default=sa.func.current_timestamp(),
                            nullable=False, index=True)

    weixin = sa.relationship(
        'WeixinMappingModel',
        backref=db.backref('account', lazy='joined', innerjoin=True),
        primaryjoin='WeixinMappingModel.ukey==AccountModel.ukey', uselist=False,
        foreign_keys='[WeixinMappingModel.ukey]')

    def as_dict(self, summarize=True):
        default_avatar = app.config['DEFAULT_AVATAR_HASHKEY']
        result = {
            'ukey': self.ukey,
            'nickname': self.nickname,
            'gender': self.gender,
            'date_created': self.date_created.isoformat(),
        }
        return result

    @classmethod
    def create(cls, ukey, nickname):
        """
        :Parameters
            - ukey (ukey) 用户 ukey
            - nickname (unicode) 用户昵称
            - unblock (boolean) 是否重新创建 (解封)

        """
        deleted = cls.deleted.query.get(ukey)
        # 检查用户是否是复活回来的
        if deleted is not None:
            raise Exception('帐号被封禁, 不能创建用户')
        # 全新的用户
        user = UserModel(ukey=ukey, nickname=nickname)
        db.session.add(user)

        # 提交一次, 如果冲突直接抛错回滚
        db.session.commit()

        return user

    @classmethod
    def delete(cls, ukey):
        """
        :Parameters
            - ukey (ukey) 用户 ukey

        """
        user = cls.query.get(ukey)
        # 静默处理
        if user:
            db.session.delete(user)
            db.session.commit()

