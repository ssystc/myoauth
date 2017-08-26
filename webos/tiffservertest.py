#coding=utf-8

import requests
import M2Crypto
import config
import base64
import json
import requests
import json
import os
import time
import urllib2
import poster.encode
import poster.streaminghttp
import simplejson
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode
import traceback


# token = 'C2AiaeBba1eSKL6cl21+yh7GZcJ94FRMtLBJTMFx3AqyLokamNidIJTgiAunaoInIeK1SJ9M23AWOGmhFAloeYrbsY9JfVI+uhvvxTF0B64w+4qBf5kgUdLr1RI1TEmMryWBNjLSyyBi2aEc3FtYoKrBs/VhMxhaDssKwJ0+hHA='

# def queryData(metadataid, token):
#     try:
#         urlBasemetadataid = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_QUERY_URL % (metadataid, token))
#         print urlBasemetadataid
#
#         rep = requests.get(urlBasemetadataid)
#         querymessage = json.loads(rep.content)
#         print querymessage
#
#
#         querypath = querymessage['queryPath']
#         queryparams = (json.loads(querymessage['queryParams']))['id']
#         # print querypath
#         # print queryparams
#
#
#         urlBasequerymessage = 'http://%s%s%s?id=%s&token=%s' % (
#         config.TIFF_DATA_HOST, config.TIFF_DATA_BASEQUERY_URL, querypath, queryparams, token)
#         # print urlBasequerymessage
#
#         print urlBasequerymessage
#
#         rep = requests.get(urlBasequerymessage)
#         message = rep.content
#
#         return message
#     except:
#         config.Log.info(traceback.format_exc())
#         return None
#
# # print queryData('19fbd18d-78cc-45f7-aa3f-64ddf21c6872', token)
#
# def queryProductLayerName(metadataid, token):
#     message = json.loads(queryData(metadataid, token))
#     print message
#     message = message['sliceTasks']
#     if message:
#         for info in message:
#             if info['mimeType'] == 'product':
#                 return info['layerName']
#
#     else:
#         config.Log.info("can't get metadata information or info has no layername attribute, metadataid = %s" % metadataid)
#         return None
# # print queryProductLayerName('19fbd18d-78cc-45f7-aa3f-64ddf21c6872',token)
#
#
#
# def queryPngLayerName(metadataid, token):
#     message = json.loads(queryData(metadataid, token))
#     message = message['sliceTasks']
#     if message:
#
#         for info in message:
#
#             if info['mimeType'] == 'png':
#                 return info['layerName']
#
#     else:
#         config.Log.info("can't get metadata information or info has no layername attribute, metadataid = %s" % metadataid)
#         return None
#
#
#
# def queryDataUrl(metadataid, token):
#     layerName = queryProductLayerName(metadataid, token)
#     if layerName:
#         return 'info="http://%s%s%s",data="http://%s%s%s"' % (config.IMG_SERVER_HOST, config.IMG_SERVER_INFO_URL, layerName, config.IMG_SERVER_HOST, config.IMG_SERVER_DATA_URL, layerName)
#     else:
#         return None



a = '0d894851-2372-499d-a3be-23b0943428a1'
# print queryDataUrl(a, token)

# rep = requests.get('http://192.168.4.3:8808/metadata-service/metadata/manage/id?id=ce280255-4fad-44ee-91a6-783f97d7385d&token=DsQUtLFAcEO+HMVcpU9jHN7cyG5o6SIgiYyhL/hs2faJQZej6ZO9Z+zn4361oBzUn+bZhpCukXZyZTXVfo50Me+UBPSUkcvJQ3X7A/CdXvWReVibCGswTvJPcCoy71THzT3ALZdvCCzZMLk++dV4HOR6AS9t7Sy6lI3+NJVk3Bk=')
# print rep.content

# [{u'mimeType': u'png', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_png', u'tileType': None, u'id': 60}, {u'mimeType': u'product', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_product', u'tileType': None, u'id': 59}]
# [{u'mimeType': u'png', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_png', u'tileType': None, u'id': 60}, {u'mimeType': u'product', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_product', u'tileType': None, u'id': 59}]
#
#
#
# [{u'mimeType': u'product', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_product', u'tileType': None, u'id': 59}, {u'mimeType': u'png', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_png', u'tileType': None, u'id': 60}]
# [{u'mimeType': u'product', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_product', u'tileType': None, u'id': 59}, {u'mimeType': u'png', u'layerName': u'GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-MSS1_805_png', u'tileType': None, u'id': 60}]


# rep = requests.get('http://192.168.4.3:8808/metadata-service/metadata/manage/id?id=0d894851-2372-499d-a3be-23b0943428a1&token=C2AiaeBba1eSKL6cl21+yh7GZcJ94FRMtLBJTMFx3AqyLokamNidIJTgiAunaoInIeK1SJ9M23AWOGmhFAloeYrbsY9JfVI+uhvvxTF0B64w+4qBf5kgUdLr1RI1TEmMryWBNjLSyyBi2aEc3FtYoKrBs/VhMxhaDssKwJ0+hHA=')
# print rep.content
#
# print '##########################################'
#
# rep = requests.get('http://192.168.4.3:8808/image-service/image/query/id?id=851&token=C2AiaeBba1eSKL6cl21+yh7GZcJ94FRMtLBJTMFx3AqyLokamNidIJTgiAunaoInIeK1SJ9M23AWOGmhFAloeYrbsY9JfVI+uhvvxTF0B64w+4qBf5kgUdLr1RI1TEmMryWBNjLSyyBi2aEc3FtYoKrBs/VhMxhaDssKwJ0+hHA=')
# print rep.content

# rep = requests.post('http://192.168.4.3:8808/metadata-service/metadata/manage/id',
#                     data={
#                         'id': '0d894851-2372-499d-a3be-23b0943428a1',
#                         'token': 'C2AiaeBba1eSKL6cl21+yh7GZcJ94FRMtLBJTMFx3AqyLokamNidIJTgiAunaoInIeK1SJ9M23AWOGmhFAloeYrbsY9JfVI+uhvvxTF0B64w+4qBf5kgUdLr1RI1TEmMryWBNjLSyyBi2aEc3FtYoKrBs/VhMxhaDssKwJ0+hHA='
#                     })
# print rep.content
#
# rep = requests.post('http://192.168.4.3:8808/image-service/image/query/id',
#                     data={
#                         'id': 851,
#                         'token': 'C2AiaeBba1eSKL6cl21+yh7GZcJ94FRMtLBJTMFx3AqyLokamNidIJTgiAunaoInIeK1SJ9M23AWOGmhFAloeYrbsY9JfVI+uhvvxTF0B64w+4qBf5kgUdLr1RI1TEmMryWBNjLSyyBi2aEc3FtYoKrBs/VhMxhaDssKwJ0+hHA='
#                     })
# print rep.content

def queryData(metadataid, token):
    rep = requests.post('http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_QUERY_BY_METAID),
                        data={
                            'id': metadataid,
                            'token': token
                        })
    message = json.loads(rep.content)
    imageId = json.loads(message['queryParams'])['id']

    nextrep = requests.post('http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_QUERY_BY_TIFFID),
                            data={
                                'id': imageId,
                                'token': token
                            })
    nextmessage = nextrep.content
    return nextmessage

def queryProductLayerName(metadataid, token):
    try:
        message = json.loads(queryData(metadataid, token))
        message = message['sliceTasks']
        if message:
            for info in message:
                if info['mimeType'] == 'product':
                    return info['layerName']

        else:
            config.Log.info("can't get metadata information or info has no layername attribute, metadataid = %s" % metadataid)
            return None
    except:
        config.Log.info(traceback.format_exc())
        raise MsgException(ErrorCode.FindTiffDataError, u'get tiff layername error: %s' % traceback.format_exc())



def queryDataUrl(metadataid, token):
    layerName = queryProductLayerName(metadataid, token)
    if layerName:
        return 'info="http://%s%s%s",data="http://%s%s%s"' % (config.IMG_SERVER_HOST, config.IMG_SERVER_INFO_URL, layerName, config.IMG_SERVER_HOST, config.IMG_SERVER_DATA_URL, layerName)
    else:
        return None


# print queryData('7135e72f-89d0-475c-ae35-21bddfa9cd9d', 'C2AiaeBba1eSKL6cl21+yh7GZcJ94FRMtLBJTMFx3AqyLokamNidIJTgiAunaoInIeK1SJ9M23AWOGmhFAloeYrbsY9JfVI+uhvvxTF0B64w+4qBf5kgUdLr1RI1TEmMryWBNjLSyyBi2aEc3FtYoKrBs/VhMxhaDssKwJ0+hHA=')
print queryDataUrl('cb780731-0078-4b8d-b0b2-57fb9c3887af', 'egZlYJ/dxhpEIXokQaz5L3HxnBSK6ZDmHKnEUV9mCbXr6eTTQHmoe7SlfTIg4gZSB1MnEGA/gwYeHeGrEKVJhutmBMx7E9HDsoO2W6dQ9nCDwVVOGlbtiprU1IzMuO21OtcMfAaovhld/Zn3m/aFQ9V3LBRU+5amXlWORb8zhko=')



