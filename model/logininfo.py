#coding=utf-8

from sqlalchemy import Float, String, Column
from model import Base, session_scope

class LoginInfo(Base):
    __tablename__ = 'logininfo'

    uid = Column(String, primary_key=True)
    token = Column(String)
    refreshtoken = Column(String)
    userid = Column(String)
    username = Column(String)
    time = Column(Float)

    def __init__(self, uid, token, refreshtoken, userid, username, time):
        self.uid = uid
        self.token = token
        self.refreshtoken = refreshtoken
        self.userid = userid
        self.username = username
        self.time = time

class LoginInfoDao(object):

    @classmethod
    def add(cls, userinfo):
        with session_scope() as session:
            session.add(userinfo)
        return userinfo.uid

    @classmethod
    def queryByuid(cls,uid):
        with session_scope() as session:
            try:
                return session.query(LoginInfo).filter(LoginInfo.uid == uid).one()
            except:
                return None

    @classmethod
    def deleteByuserid(cls,userid):
        with session_scope() as session:
            session.query(LoginInfo).filter(LoginInfo.userid == userid).delete()

    @classmethod
    def deleteAll(cls):
        with session_scope() as session:
            session.query(LoginInfo).filter().delete()

    @classmethod
    def getUserId(cls, uid):
        info = cls.queryByuid(uid)
        return info.userid if info else ''