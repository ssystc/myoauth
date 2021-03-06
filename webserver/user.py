# coding: utf-8

import requests
import uuid
import flask
import base64
import json
import functools
import config
import M2Crypto
import time
from model.logininfo import LoginInfoDao, LoginInfo
from model.redirect import RedirectDao, Redirect
# from webserver import app
from flask import Flask
# from common.const import ErrorCode
import traceback
import socket
import model


def decrypt(access_token):
    bio = M2Crypto.BIO.MemoryBuffer(config.PUBLIC_KEY)
    pkey = M2Crypto.RSA.load_pub_key_bio(bio)
    token = pkey.public_decrypt(base64.decodestring(
        access_token),M2Crypto.RSA.no_padding)
    return token.strip('\x00')

def getMyIP():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

app=Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.route('/user/login', methods=['GET'])
def login():
    uid = uuid.uuid4().hex
    flask.session['uid'] = uid
    loginurl = 'https://%s%s' % (config.OAUTH_URL, config.OAUTH_LOGIN_URL %
                                 (config.CLIENT_ID, config.OAUTH_REDIRECT_URL, uid))
    # loginurl = "https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/authorize?client_id=200010035116400&redirect_uri=http://127.0.0.1:8888/user/logincallback/%s&response_type=code" % uid
    return flask.redirect(loginurl)

@app.route('/user/logincallback/<uid>')
def autho(uid):
    try:
        code = flask.request.args['code']
        rep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_REQUIRE_TOKEN_URL),
                    data={'client_id': config.CLIENT_ID, 'code': code, 'grant_type': 'authorization_code',
                          'ip': getMyIP()},
                    verify=False)

        repmessage = json.loads(rep.content)
        token_nodecrypt = repmessage['access_token']
        refresh_token_nodecrypt = repmessage['refresh_token']
        token_crypt = decrypt(token_nodecrypt)

        verifyrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                                  data={'client_id': config.CLIENT_ID, 'token': token_crypt},
                                  verify=False)

        verifymessage = json.loads(verifyrep.content)

        if verifymessage['errors_code'] == 0:
            user_id = verifymessage['userID']
            user_name = verifymessage['username']
            LoginInfoDao.deleteByuserid(user_id)
            login_info = LoginInfo(uid, token_nodecrypt, refresh_token_nodecrypt, user_id, user_name, time.time())
            LoginInfoDao.add(login_info)
            url = flask.url_for('test')
            return flask.redirect(url)

        else:
            return flask.jsonify({'code': 'can not login','errors_code': verifymessage['errors_code']})


    except:
        # config.Log.info(traceback.format_exc())
        return flask.jsonify({'code': 'can not login'})     #can not login出现时别忘了把他替换成ErrorCode.logingError

# def needLogin():
#     try:
#         uid = flask.session['uid']
#         logininfo = LoginInfoDao.queryByuid(uid)
#         token = decrypt(logininfo.token)
#         refreshtoken = logininfo.refreshtoken
#         verifyrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
#                                   data={'client_id': config.CLIENT_ID, 'token': token},
#                                   verify=False)
#         verifymessage = json.loads(verifyrep.content)
#         if verifymessage['errors_code'] == 0:
#             return False
#         if verifymessage['errors_code'] == 10004002:
#             #需要在数据库中更新token和refreshtoken
#             refreshrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_REQUIRE_TOKEN_URL),
#                                        data={'grant_type': 'refresh_token', 'refresh_token': refreshtoken,
#                                              'client_id': config.CLIENT_ID},
#                                        verify=False
#                                        )
#             newtokenmessage = json.loads(refreshrep.content)
#             newtoken = newtokenmessage['access_token']
#             newtoken_crypt = decrypt(newtoken)
#             newrefreshtoken = newtokenmessage['refresh_token']
#
#             newverifyrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
#                                       data={'client_id': config.CLIENT_ID, 'token': newtoken_crypt},
#                                       verify=False)
#             newverifymessage = json.loads(newverifyrep.content)
#
#             if newverifymessage['errors_code'] == 0:
#                 user_id = newverifymessage['userID']
#                 user_name = newverifymessage['username']
#                 LoginInfoDao.deleteByuserid(user_id)
#                 login_info = LoginInfo(uid, newtoken, newrefreshtoken, user_id, user_name, time.time())
#                 LoginInfoDao.add(login_info)
#                 return False
#             else:
#                 return True
#         else:
#             return True
#     except:
#         return True
def needLogin():
    try:

        if flask.request.form.get('token'):
            token = flask.request.form.get('token')
            token = decrypt(token)                      #需不需要我自动更新呢
            verifyrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                                    data={'client_id': config.CLIENT_ID, 'token': token},
                                    verify=False)
            verifymessage = json.loads(verifyrep.content)
            if verifymessage['errors_code'] == 0:
                return False
        else:
            uid = flask.session['uid']
            logininfo = LoginInfoDao.queryByuid(uid)
            token = decrypt(logininfo.token)
            refreshtoken = logininfo.refreshtoken
            verifyrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                                      data={'client_id': config.CLIENT_ID, 'token': token},
                                      verify=False)
            verifymessage = json.loads(verifyrep.content)
            if verifymessage['errors_code'] == 0:
                return False
            if verifymessage['errors_code'] == 10004002:
                # 需要在数据库中更新token和refreshtoken
                refreshrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_REQUIRE_TOKEN_URL),
                                            data={'grant_type': 'refresh_token', 'refresh_token': refreshtoken,
                                                    'client_id': config.CLIENT_ID},
                                            verify=False
                                           )
                newtokenmessage = json.loads(refreshrep.content)
                newtoken = newtokenmessage['access_token']
                newtoken_crypt = decrypt(newtoken)
                newrefreshtoken = newtokenmessage['refresh_token']

                newverifyrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                                            data={'client_id': config.CLIENT_ID, 'token': newtoken_crypt},
                                            verify=False)
                newverifymessage = json.loads(newverifyrep.content)
                if newverifymessage['errors_code'] == 0:
                    user_id = newverifymessage['userID']
                    user_name = newverifymessage['username']
                    LoginInfoDao.deleteByuserid(user_id)
                    login_info = LoginInfo(uid, newtoken, newrefreshtoken, user_id, user_name, time.time())
                    LoginInfoDao.add(login_info)
                    return False
                else:
                    return True
            else:
                return True
    except:
        return True


def login_required(func):
    '''测试登陆状态，如果未登陆则跳转到登陆页面'''
    @functools.wraps(func)
    def decoratedFunc(*args, **kwargs):
        if needLogin():
            return flask.abort(401)
        return func(*args, **kwargs)
    return decoratedFunc



@app.route('/', methods=['GET'])
@login_required
def test():
    # token = flask.request.form.get('token')
    # if token:
    #     return flask.jsonify({
    #         'code': 0,
    #         'token': token
    #     })
    return 'success'


    # logininfoclass = model.logininfo.LoginInfo('111', 'adgqwetgds', 'wqertfdsaf', 'useridadf',
    #                                            'ssy', time.time())
    # model.logininfo.LoginInfoDao.add(logininfoclass)


@app.route('/user/queryusername', methods=['GET'])
@login_required
def queryUsername():
    uid = flask.session['uid']
    login_info = LoginInfoDao.queryByuid(uid)
    if login_info:
        return flask.jsonify({'username': login_info.username, 'code': 0})
    else:
        return flask.jsonify({'code': -601})

@app.route('/user/logout', methods=['GET'])
def logout():
    uid = flask.session['uid']
    if LoginInfoDao.queryByuid(uid):
        flask.session['uid'] = ''
        return flask.jsonify({'code': 0})
    else:
        return flask.jsonify({'code': -602})


app.run('127.0.0.1',8888)






