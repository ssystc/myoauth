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
import model.userinfo






# model.userinfo.userInfoDao.addUserInfoDict(mydict)
#
# model.userinfo.userInfoDao.queryall()
# userinfoclass=model.userinfo.userInfo('5','3','2314',2)
# print model.userinfo.userInfoDao.addUserInfo(userinfoclass)

print model.userinfo.UserInfoDao.queryByuid('79132ccf-1f39-41e1-b85a-05b8b35571cb')

# print model.userinfo.userInfoDao.deleteByuserid('1')