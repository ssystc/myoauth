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
from webserver import app
from common.const import ErrorCode
import traceback


def decrypt(access_token):
    bio = M2Crypto.BIO.MemoryBuffer(config.PUBLIC_KEY)
    pkey = M2Crypto.RSA.load_pub_key_bio(bio)
    token = pkey.public_decrypt(base64.decodestring(
        access_token), M2Crypto.RSA.no_padding)
    return token.strip('\x00')


@app.route('/user/login', methods=['GET'])
def login():
    uid = uuid.uuid4().hex
    flask.session['uid'] = uid
    if 'redirect' in flask.request.args:
        prams = ['%s=%s' % (arg, flask.request.args[arg]) for arg in flask.request.args if arg != 'redirect']
        if prams:
            rurl = '%s&%s' % (flask.request.args['redirect'], '&'.join(prams))
        else:
            rurl = flask.request.args['redirect']

        redirect = Redirect(uid, rurl)
        RedirectDao.add(redirect)

    loginurl = 'https://%s%s' % (config.OAUTH_URL, config.OAUTH_LOGIN_URL %
                                 (config.CLIENT_ID, config.OAUTH_REDIRECT_URL, uid))
    return flask.redirect(loginurl)


@app.route('/user/logincallback/<uid>', methods=['GET'])
def autho(uid):
    try:
        access_token = flask.request.args['access_token']
        token = decrypt(access_token)

        rep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                            data={'client_id': config.CLIENT_ID, 'token': token},
                            verify=False
                            )

        message = json.loads(rep.content)

        if message['errors_code'] == 0:
            user_id = message["userID"]
            LoginInfoDao.deleteByuserid(user_id)
            login_info = LoginInfo(uid, access_token, user_id, time.time())
            LoginInfoDao.add(login_info)
            url = RedirectDao.pop(uid) or config.INDEX_PAGE
            return flask.redirect(url)
        else:
            return flask.jsonify({'code': ErrorCode.LoginError, 'errors_code': message['errors_code']})
    except:
        config.Log.info(traceback.format_exc())
        return flask.jsonify({'code': ErrorCode.LoginError})


def needLogin():
    try:
        uid = flask.session['uid']
        logininfo = LoginInfoDao.queryByuid(uid)
        token = decrypt(logininfo.token)
        rep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                            data={'client_id': config.CLIENT_ID, 'token': token},
                            verify=False)

        message = json.loads(rep.content)
        return message['errors_code'] != 0
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


def getUserId():
    if 'uid' in flask.session:
        return LoginInfoDao.getUserId(flask.session['uid'])
    else:
        return ''