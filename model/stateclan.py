# coding: utf-8

from . import Base, session_scope
from sqlalchemy import Integer, Float, String, UnicodeText, Column, ForeignKey, desc
from sqlalchemy.orm import relationships

import uuid
import json

class StateClan(Base):

    __tablename__ = 'stateclan'

    uid = Column(String, primary_key=True)
    # taskId = Column(String, ForeignKey('task.id'))
    taskId = Column(String)
    clan = Column(UnicodeText)
    userId = Column(String)
    name = Column(String)
    time = Column(Float)

    # task = relationships('Task', back_populates='stateclans')

    def __init__(self, uid, taskId, clan, userId, name, time):
        self.uid = uid
        self.taskId = taskId
        self.clan = unicode(json.dumps(clan, ensure_ascii=False)) if isinstance(clan, dict) else clan
        self.userId = userId
        self.name = name
        self.time = time

class StateClanDao(object):

    @classmethod
    def addStateClan(cls, stateclan):
        with session_scope() as session:
            session.add(stateclan)
        return stateclan.uid

    @classmethod
    def queryClanByUid(cls, uid, userId):
        with session_scope() as session:
            try:
                stateclan = session.query(StateClan).filter(StateClan.uid == uid, StateClan.userId == userId).one()
                return stateclan.clan
            except:
                return None

    @classmethod
    def queryClanByTaskid(cls, taskId, userId):
        clanList = []
        with session_scope as session:
            try:
                stateclans = session.query(StateClan).filter(StateClan.taskId == taskId, StateClan.userId == userId).all()
                for info in stateclans:
                    clanList.append(info.clan)
                return clanList
            except:
                return None

    @classmethod
    def deleteByTaskId(cls, taskId, userId):
        with session_scope() as session:
            session.query(StateClan).filter(StateClan.taskId == taskId, StateClan.userId == userId).delete()

    @classmethod
    def queryByTaskId(cls, taskId, userId):
        try:
            with session_scope() as session:
                infolist = session.query(StateClan).filter(StateClan.taskId == taskId, StateClan.userId == userId).order_by(StateClan.time).all()
                return infolist
        except:
            return None








