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
import model
import model.userinfo




def jiemi(token):
    bio = M2Crypto.BIO.MemoryBuffer(config.PUBLIC_KEY)
    pkey = M2Crypto.RSA.load_pub_key_bio(bio)
    token_nojiemi = token
    token_jiemi = pkey.public_decrypt(base64.decodestring(token_nojiemi), M2Crypto.RSA.no_padding)

    def decodeResult(info):
        content = ''
        for i in info:
            if not i == '\x00':
                content = content + i
        return content
    mytoken = decodeResult(token_jiemi)
    return mytoken


app=Flask(__name__)
app.secret_key = config.SECRET_KEY



@app.route('/user/login')
def login():
    uid = uuid.uuid4().hex
    session['uid']=uid
    # myurl = "https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/authorize?client_id=200010035116400&redirect_uri=http://127.0.0.1:8888/user/logincallback/%s&response_type=token" % uid
    myurl='https://%s%s'  % (config.OAUTH_URL,config.OAUTH_LOGIN_URL % (config.CLIENT_ID,config.OAUTH_REDIRECT_URL,uid))
    return make_response(redirect(myurl))


@app.route('/user/logincallback/<uid>')
def autho(uid):

    token_nojiemi = request.args['access_token']
    final_token=jiemi(token_nojiemi)
    print final_token
    re = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                       data={'client_id': config.CLIENT_ID, 'token': final_token},
                       verify=False
                       )
    message=re.content
    message = json.loads(message)
    userID = message["userID"]

    model.userinfo.UserInfoDao.deleteByuserid(userID)

    userinfo=model.userinfo.UserInfo(uid,token_nojiemi,userID,time.time())
    model.userinfo.UserInfoDao.addUserInfo(userinfo)

    return flask.redirect(flask.url_for('test'))

    # return u'用户%s成功登陆' % (userID)



def needLogin():
    if not 'uid' in flask.session:
        return True

    uid=session['uid']
    print 'find uid %s' % uid
    myuserInfo=model.userinfo.UserInfoDao.queryByuid(uid)        #queryByuid
    print myuserInfo
    if myuserInfo==None:
        return True
    else:
        token_nojiemi=myuserInfo.token
        final_token=jiemi(token_nojiemi)
        # re = requests.post("https://192.168.4.225:8443/user_oauth/oauth-server-idp/verify2",
        #                     data={'client_id': '200010035116400', 'token': final_token},
        #                     verify=False)
        re=requests.post('https://%s%s' % (config.OAUTH_URL,config.OAUTH_VARIFY_URL),
                         data={'client_id':config.CLIENT_ID, 'token':final_token},
                         verify=False
                         )

        message = re.content
        message = json.loads(message)
        if not message["errors_code"]==0:
            return True

    return False



def login_required(func):
    '''测试登陆状态，如果未登陆则跳转到登陆页面'''
    @functools.wraps(func)
    def decoratedFunc(*args, **kwargs):
        if needLogin():
            return abort(401)
        return func(*args, **kwargs)
    return decoratedFunc


@app.route('/')
@login_required
def test():
    return flask.session['uid']

# print model.userinfo.UserInfoDao.queryByuid('79132ccf-1f39-41e1-b85a-05b8b35571cb')
app.run('127.0.0.1',8888)

