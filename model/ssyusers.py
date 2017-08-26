
import uuid
import json

from sqlalchemy import Integer, Float, String, UnicodeText, Column, ForeignKey
from sqlalchemy.orm import relationship
from model import Base,session_scope
import traceback
from sqlalchemy.orm import sessionmaker



class User(Base):
    __tablename__ = 'ssyusers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    addresses = relationship("Address",
                             back_populates='user',
                             cascade="all, delete, delete-orphan")



class Address(Base):
    __tablename__ = 'ssyaddresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('ssyusers.id'))

    user = relationship("User",
                        back_populates="addresses")


with session_scope as session:
    zhang = session.query(User).get(1)
print zhang