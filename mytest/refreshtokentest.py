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


app=Flask(__name__)
app.secret_key = config.SECRET_KEY

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


@app.route('/')
def login():
    rep = make_response(redirect(
        "https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/authorize?client_id=200010035116400&redirect_uri=http://127.0.0.1:8888/tok&response_type=code"))
    return rep


@app.route('/tok')
def v_login():
    # token_weijiemi = request.args['access_token']
    # token_jiemi=jiemi(token_weijiemi)
    #
    # re = requests.post("https://192.168.4.225:8443/user_oauth/oauth-server-idp/verify2", data={'client_id': '200010035116400', 'token': token_jiemi},
    #                        verify=False)
    #
    # message=re.text
    # message=json.loads(message)
    # message=message["userID"]


    code=request.args['code']

    print code

    rep = requests.post("https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/access_token",
                        data={'client_id': '200010035116400', 'code': code, 'grant_type': 'authorization_code', 'ip':'192.168.44.63'},
                        verify=False)

    # rep = make_response(redirect("https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/access_token?client_id=200010035116400&code=%s&response_type=authorization_code" % code))

    return rep.text


token='ekAZrlf0A3rIOrVGHCzgXCxorqP337ydXWq0KRjA1b7iZ8CUhvlAb9W589gfmsfjye0I0k0UOQZ0oA8csOpq2UnmWUIdE0sOCI3ZnShasoTU3UKZmOU+iDgLnNdCirGzBOwJSe0JGG9qIoP9l4SJ3YBAJPlJNLiMorcHv8wCywM='
refreshtoken='z//T9+9KSqFQbTiaPhvMrJEv2HTDp3C0t4calLygMHOTpFNlW/nvvcq9seMhsZcWdE/uH/u1z5GsbHhshez4tvs6sKoMGqFMQByFnZBrhGW7o45JAAgTRR/MSglnBb9j1IXSwKnzqQvPT9dEeJ5pkOix16oXejHThsAlwF9J2FY='

token_jiemi=jiemi(token)
refreshtoken_jiemi=jiemi(refreshtoken)

print token_jiemi
print refreshtoken_jiemi

refreshrep=requests.post('https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/access_token',
                         data={'grant_type':'refresh_token', 'refresh_token':refreshtoken_jiemi, 'client_id': '200010035116400'},
                         verify=False
                         )
print refreshrep.text

# verifyrep=requests.post("https://192.168.4.225:8443/user_oauth/oauth-server-idp/verify2",
#                         data={'client_id': '200010035116400', 'token': token_jiemi},
#                         verify=False)
#
# print verifyrep.text







# app.run('127.0.0.1',8888)