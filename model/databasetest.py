#coding=utf-8

import requests
import uuid
import flask
from flask import Flask,make_response,request,session,redirect,url_for,abort
import flask_login
import base64
from Crypto.PublicKey import RSA
from Crypto import Random
import json
import functools
import config
import uuid
import M2Crypto
import time
import model.logininfo
import model.stateclan
import flask

# logininfoclass=model.logininfo.LoginInfo('111','adgqwetgds','wqertfdsaf','useridadf',
#                           'ssy',time.time())
# print model.logininfo.LoginInfoDao.add(logininfoclass)

# logindelete = model.logininfo.LoginInfoDao.deleteByuid('efdfedc4430a4910a8e0fa1afe4dc5e5')
# print logindelete


def querytest():
    stateclanList = model.stateclan.StateClanDao.queryByTaskId('23b11623c5dc4e0f99656a0856dda5d7', '200010035324693')
    print stateclanList
    if not stateclanList:
        code = 111
        return flask.jsonify({'code': code})

    message = {}
    for info in stateclanList:
        message[info.name] = {'clan': info.clan}
    return message

print querytest()


