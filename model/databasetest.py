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

logininfoclass=model.logininfo.LoginInfo('111','adgqwetgds','wqertfdsaf','useridadf',
                          'ssy',time.time())
print model.logininfo.LoginInfoDao.add(logininfoclass)