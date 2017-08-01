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
import socket


# re = requests.post("https://192.168.4.225:8443/user_oauth/oauth-server-idp/verify2",
#                    data={'client_id': '200010035116400', 'token': 'dagafadsgasdfd'},
#                    verify=False)
#
# message=re.text
# message = json.loads(message)
# print message["message"]
# if message['message']=="Token not found":
#     print 'meiyoutoken'


token_nojiemi='rt/G6GCFHHRn4E0qLuMIxTRK7od+HB3yHu2x51VKkDkUidYeU1xpn7PqMuz7WLVIs3FnkZLKo/e/ITJ0/jdnoauyNixpvUuPYcY5bvY+5cell5AMdIed20lnAmmQKs5UasMXHxFQ3jszrHkgeLgsLOwxNnXz0E4+ldQ+C90IgnI='
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

# token_nojiemi="gg2hGtEC/zD3VjVJqwasz3KYIVxuGL4JNbwJKGWlDGVFPYeOV/4Br4iRU93IYRelfmyBcw3qdzj6jHA9E1a6plRY/snzozCibaEVtFUdIVpKFBXikTsWrzyO55udCPZnJyZjPY31eSbWboivVS9hWaTVYzfXUcnggm4Rk0HwHiQ="
final_token=jiemi(token_nojiemi)
# print final_token
# re = requests.post("https://192.168.4.225:8443/user_oauth/oauth-server-idp/verify2",
#                    data={'client_id': '200010035116400', 'token':final_token },
#                    verify=False)
# print re.text

# print type(time.time())

# token='14.1011c340-8cfc-466a-a132-684f87320e6a'
#
# re=requests.post('https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/refresh_token',
#                  data={'grant_type':'refresh_token','refresh_token':'14.1011c340-8cfc-466a-a132-684f87320e6a'}
#                  )

def getMyIP():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip
print getMyIP()
