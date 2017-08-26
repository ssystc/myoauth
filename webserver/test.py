#coding = utf-8

import requests
import config
import json
import webserver.user
from model.logininfo import LoginInfoDao
import M2Crypto
import base64

# rep = requests.post(url = 'http://127.0.0.1:8888/', data={'token': '+wZkjRn4Qz317ev5pe/LdFeXM40f9ii4viO4uAI='})
# print rep.content


def crypt(access_token):
    bio = M2Crypto.BIO.MemoryBuffer(config.PUBLIC_KEY)
    pkey = M2Crypto.RSA.load_pub_key_bio(bio)
    token = pkey.public_decrypt(base64.decodestring(
        access_token),M2Crypto.RSA.no_padding)
    return token.strip('\x00')


def getTokenByuserid(userid):
    try:
        logininfo = LoginInfoDao.queryByuserid(userid)
        token = logininfo.token
        token_crypt = crypt(token)
        refreshtoken = logininfo.refreshtoken
        verifyrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_VARIFY_URL),
                                  data={'client_id': config.CLIENT_ID, 'token': token_crypt},
                                  verify=False)

        verifymessage = json.loads(verifyrep.content)
        if verifymessage['errors_code'] == 0:
            return token_crypt
        elif verifymessage['errors_code'] == 10004002:
            refreshrep = requests.post('https://%s%s' % (config.OAUTH_URL, config.OAUTH_REQUIRE_TOKEN_URL),
                                       data={'grant_type': 'refresh_token', 'refresh_token': refreshtoken,
                                             'client_id': config.CLIENT_ID},
                                       verify=False
                                       )
            newtokenmessage = json.loads(refreshrep.content)
            newtoken = newtokenmessage['access_token']
            newtoken_crypt = crypt(newtoken)
            return newtoken_crypt
        else:
            return None

    except:
        return None

print getTokenByuserid('200010035116700')