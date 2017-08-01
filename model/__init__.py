#coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from config import DB_ADDRESS,Log
import traceback


engine=create_engine(DB_ADDRESS,echo=False)
Base=declarative_base()
Session=sessionmaker(bind=engine,expire_on_commit=False)

@contextmanager
def session_scope():
    session=Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()


import model.userinfo
import model.logininfo

Base.metadata.create_all(engine)


