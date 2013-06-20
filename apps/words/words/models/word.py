#!/usr/bin/env python
# encoding: utf-8

import sqlalchemy as sa
from words.database import ModelBase


class WordModel(ModelBase):
    __tablename__ = 'word'

    id = sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    word = sa.Column('word', sa.Unicode(256), default='',
                      server_default='', nullable=False)
    meaning = sa.Column('meaning', sa.Unicode(1024),
                             default='', server_default='', nullable=False)
    source = sa.Column('source', sa.Unicode(256), nullable=False, unique=True)
    native = sa.Column('native', sa.Unicode(256), nullable=False, unique=True)
    date_created = sa.Column('date_created', sa.DateTime(timezone=True),
                            server_default=sa.func.current_timestamp(),
                            nullable=False, index=True)


class VocabularyModel(ModelBase):
    __tablename__ = 'vocabulary'

    id = sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    ukey_owner = sa.Column('ukey_owner',
            sa.CHAR(6), nullable=False, index=True)
    title = sa.Column('title', sa.Unicode(256), nullable=False, unique=True)
    cover = sa.Column('avatar', "db.HashkeyType()", nullable=True)
    summary = sa.Column('summary', sa.Unicode(1024),
            default='', server_default='', nullable=False)
    date_created = sa.Column('date_created', sa.DateTime(timezone=True),
                            server_default=sa.func.current_timestamp(),
                            nullable=False, index=True)

    wordship = sa.relationship(
        'WordshipModel',
        primaryjoin='WordshipModel.vocabulary_id==VocabularyModel.id',
        order_by='desc(VocabularyModel.title)',
        backref=sa.backref(
        'words', lazy='joined', innerjoin=True),
        foreign_keys='[WordshipModel.vocabulary_id]',
        passive_deletes='all', lazy='dynamic')


class WordshipModel(ModelBase):
    __tablename__ = 'wordship'

    word_id = sa.Column('word_id', sa.Integer(), nullable=False,
            index=True, primary_key=True)
    vocabulary_id = sa.Column('vocabulary_id ',
            sa.Integer(), nullable=False, index=True, primary_key=True)
    date_created = sa.Column('date_created', sa.DateTime(timezone=True),
                                server_default=sa.func.current_timestamp(),
                                nullable=False, index=True)


class PlanModel(ModelBase):
    __table__ = 'plan'

    id = sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    outline = sa.Column('outline', sa.Enum('ebbinghaus', 'weekly', \
            name='plan_outline_enum'), nullable=False)
    ukey_owner = sa.Column('ukey_owner', sa.CHAR(6),
            sa.ForeignKey('account.ukey'), nullable=False, index=True)
    vocabulary_id = sa.Column('vocabulary_id',
            sa.Integer(), nullable=False, index=True)
    date_lasest_active = sa.Column('date_lasest_active',
            sa.DateTime(timezone=True),
            server_default=sa.func.current_timestamp(),
            nullable=False, index=True)
    date_created = sa.Column('date_created', sa.DateTime(timezone=True),
                                server_default=sa.func.current_timestamp(),
                                nullable=False, index=True)
