#coding=utf-8

import uuid
import json

from sqlalchemy import Integer, Float, String, UnicodeText, Column, ForeignKey
from sqlalchemy.orm import relationship
from model import Base,session_scope
import traceback

class UserInfo(Base):
    __tablename__='userinfo'

    __table_args__ = {'extend_existing': True}

    uid=Column(String,unique=True,primary_key=True)
    token=Column(String)
    userid=Column(String)
    starttime=Column(Float)

    def __init__(self,uid,token,userid,starttime):
        self.uid=uid
        self.token=token
        self.userid=userid
        self.starttime=starttime




class UserInfoDao(object):
    @classmethod
    def addUserInfo(cls,userinfo):
        with session_scope() as session:
            session.add(userinfo)
            return userinfo.uid
        return None


    @classmethod
    def queryByuid(cls, uid):
        with session_scope() as session:
            try:
                return session.query(UserInfo).filter(UserInfo.uid==uid).one()
            except:
                traceback.print_exc()
                return None


    @classmethod
    def deleteByuserid(cls, userid):
        with session_scope() as session:
            try:
                deleuserinfo = session.query(UserInfo).filter(UserInfo.userid==userid).one()
                session.delete(deleuserinfo)
                return 'success'
            except:
                return 'failed'

    @classmethod
    def querytokenByusername(cls, username, userId):
        with session_scope() as session:
            try:
                return session.query().filter(Task.flowId == flowId, Task.userId == userId).all()
            except:
                return []





