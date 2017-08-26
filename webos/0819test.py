#coding=utf-8

import config
import requests
import json
import traceback

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


refreshtoken = 'DUSWLEUfDcBnrrIQh792orTPXv8/FJ9eH6UOAVQujfO6zZDytdfCQ1JeqSU9temu0HP6sfQFeZOyXZYOsrmajjHKJ2YJj/1UcUPjsqBbMsEOfJy0WdYmflbPPHbk7O9NS1Jj3IvtNBx31q2FZMnJPecShR2gCjq0jblAHgB4dY8='
metadataid = "13559756-80bb-45a2-aec7-a393d8eb6f27"

headers = {'content-type': 'application/x-www-form-urlencoded'}

# headers = None


def getNewToken():
    refreshrep=requests.post('https://192.168.4.225:8443/user_oauth/oauth-server-idp/oauth2/access_token',
                             data={'grant_type':'refresh_token', 'refresh_token':refreshtoken, 'client_id': '200010035326904'},
                             verify=False
                             )
    token = json.loads(refreshrep.content)['access_token']
    return token
print getNewToken()

for i in range(10000):

    print '################################################################'
    print 'test count: %d' % i

    token = getNewToken()
    url = 'http://192.168.4.3:8808/metadata-service/metadata/manage/id'
    rep = requests.get(url, headers=headers, params={
        'id': metadataid,
        'token': token
    })
    try:
        message = json.loads(rep.content)
        queryPath = message['queryPath']
        queryParam = json.loads(message['queryParams'])['id']
        urlBasequerymessage = 'http://%s%s%s?id=%s&token=%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_BASEQUERY_URL, queryPath, queryParam, token)
    except:
        print u'获取查询路径失败'
        print "url: %s" % url
        print "message: %s" % rep.content
        traceback.print_exc()

    try:
        finalrep = requests.get(urlBasequerymessage, headers=headers)
        finalmessage = json.loads(finalrep.content)['sliceTasks']
        print finalmessage
    except:
        print u"获取layername失败"
        print "url: %s" % urlBasequerymessage
        print "message: %s" % finalrep.content
        traceback.print_exc()

    print ''
    print ''

