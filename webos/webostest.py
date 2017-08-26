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
import flask



def decrypt(access_token):
    bio = M2Crypto.BIO.MemoryBuffer(config.PUBLIC_KEY)
    pkey = M2Crypto.RSA.load_pub_key_bio(bio)
    token = pkey.public_decrypt(base64.decodestring(
        access_token),M2Crypto.RSA.no_padding)
    return token.strip('\x00')

token = 'gfp031xh0nk5PPjcCrmJck+T6Wv9QMVlwljikNOZ2c0rHhvvZ7BAlKbQao/5Q1VSdbYNee9KOG3YvfE4uBiRAWhf3kdL7q0zZPFlYxlKjPLt3jSYHUYH1BDH09gTOcBUXwE51k0+DbjuutjdSR9vRcTelZOtEWexZbyWg53y3zw='
# token_crypt = decrypt(token)


# metadataId = 'af587879-c99b-4cce-be8e-62f35825ba3a'




# 上传Tiff文件接口
# def uploadTiffFile(fpath, mimetypes, isBase =0 ,isDem = 0):
#     config.Log.info('begin upload tiff file: %s' % fpath)
#
#     def _transSpimgToTiff(fpath):
#         spdatapath = fpath + '.data'
#         if os.path.isdir(spdatapath):
#             tiffpath = fpath + '.tiff'
#             config.Log.info('convert spimg to tiff <%s:%s>' % (fpath, tiffpath))
#             # subprocess.call("gdal_translate %s %s" % (fpath, tiffpath), shell=True)
#             subprocess.call("bash ./common/trans/trans.sh %s %s GTiff" % (fpath, tiffpath), shell=True)
#             return tiffpath
#         return fpath
#
#     try:
#         tiffpath = _transSpimgToTiff(fpath)
#
#         register_openers()
#         datagen, headers = multipart_encode({"file": open(tiffpath, "rb"),
#                                              "imageMeta.isDem": isDem,
#                                              "imageMeta.isBase": isBase,
#                                              "mimeTypes": mimetypes
#                                             })
#
#         url = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_UPLOAD_URL)
#         req = urllib2.Request(url, datagen, headers)
#
#         if tiffpath != fpath:
#             os.remove(tiffpath)
#
#         message = urllib2.urlopen(req).read()
#         obj = json.loads(message)
#
#         return obj['metadataId']
#     except:
#         print 'false'
#
# metadataid = uploadTiffFile('C:\\Users\\admin\\Desktop\\123.tiff', '11111')
# print metadataid
# print message



# 2017.8.10 tiff文件上传
# def uploadtiff(fpath, mimetypes, isBase = 0, isDem = 0):
#     register_openers()
#     datagen, headers = multipart_encode({"file": open(fpath, "rb"),
#                                          "imageMeta.isDem": isDem,
#                                          'imageMeta.isBase': isBase,
#                                          'mimeTypes': mimetypes
#                                          })
#     url = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_UPLOAD_URL)
#     req = urllib2.Request(url, datagen, headers)
#     message = urllib2.urlopen(req).read()
#     print message
#     obj = json.loads(message)
#     return obj['metadataId']

# mimetypes = json.dumps(['png','product'])
# print uploadtiff('C:\\Users\\admin\\Desktop\\tiff_image_test\\sample1_nodata.tif', mimetypes)



#查询tiff影像数据
# def queryData():
#     rep = requests.get('http://192.168.4.221:8808/image-service/image/query/id/444')
#     return rep.content
# print queryData()


# metadataId = 'e9fbf0db-2790-4d5c-8fc3-da6e02fe8e7a'
#
# rep = requests.get('http://192.168.4.221:8808/metadata-service/metadata/manage/id?id=e9fbf0db-2790-4d5c-8fc3-da6e02fe8e7a&token=asdfasdfa')
# print rep.content
# queryPath = "image/query/id/"
# queryParams = "450"
# url = 'http://192.168.4.221:8808/image-service/image/query/id/238'
# queryrep = requests.get('http://192.168.4.221:8808/image-service/image/query/id/450')
# print queryrep.content


# 在webos上创建目录
def createDir(token, username, filename, parentId, type = '1', edittype = 0):
    try:
        url = 'http://%s%s' % (config.WEBOS_DIR_HOST, config.WEBOS_MKDIR_URL)
        rep = requests.post(url, {
            'token': token,
            'filemanager.UserName': username,
            'filemanager.Name': filename,
            'filemanager.ParentID': parentId,
            'filemanager.Type': type,
            'filemanager.editType': edittype
        })
        obj = json.loads(rep.content)
        return obj['item']['items'][0]['id']
    except:
        print traceback.format_exc()
        # config.Log.info(traceback.format_exc())
        # raise MsgException(ErrorCode.CreateDirOnWebosFaild, u'create dir on webos failed.')
# print token
#
# print createDir(token, 'aaa', 'aabnnnajjeaile', '-2')


# 重命名接口
# rep = requests.post('http://192.168.44.5:8080/user_data/favorites/editFavoritesInfo',
#                     {
#                         'token': '200010035103900',
#                         'filemanager.id': '200010035330229',
#                         'filemanager.Name': 'aassd',
#                         'filemanager.ParentID': '-2'
#                     })
# print rep.content


# 查询接口
def listDir(token, dirId):
    try:
        url = 'http://%s%s' % (config.WEBOS_DIR_HOST, config.WEBOS_LISTDIR_URL)
        rep = requests.post(url, {
            'token': token,
            'parentId': dirId
        })
        obj = json.loads(rep.content)

        def _isDir(item):
            return item.get('type') == '1'

        return [{
            'id': item.get('id'),
            'path': item.get('name'),
            'type': 'dir' if _isDir(item) else 'file',
            'metadataid': item.get('metadata')
        } for item in obj['item']['items'] or []]
    except:
        config.Log.info(traceback.format_exc())
        # raise MsgException(ErrorCode.ListDirError, u"get dir list error.")

# # print token
print listDir(token, '200010035361626')



# def __uploadDir(dirid):
#     osdirs = {}
#     for d in listDir(dirid):
#         osdirs[d['path']] = d
#     return osdirs
# print __uploadDir('-1')


def queryData(metadataid, token = '200010035103900'):
    try:
        urlBasemetadataid = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_QUERY_URL % (metadataid, token))
        rep = requests.get(urlBasemetadataid)
        querymessage = json.loads(rep.content)
        querypath = querymessage['queryPath']
        queryparams = (json.loads(querymessage['queryParams']))['id']

        urlBasequerymessage = 'http://%s%s%s?id=%s' % (
        config.TIFF_DATA_HOST, config.TIFF_DATA_BASEQUERY_URL, querypath, queryparams)
        rep = requests.get(urlBasequerymessage)
        message = rep.content
        return message
    except:
        config.Log.info(traceback.format_exc())
        return None

# print queryData('013eeae1-c282-418b-a072-17b15e357e53')


# 2017.8.10 查询png切片的layername
def queryPnglayername(metadataid, token = 'tokentest'):
    message = json.loads(queryData(metadataid, token))
    message = message['sliceTasks']
    for info in message:
        if info['mimeType'] == 'png':
            return info['layerName']


# 2017.8.10 查询product切片的layername
def queryProductLayerName(metadataid, token = 'tokentest'):
    message = json.loads(queryData(metadataid, token))
    message = message['sliceTasks']
    for info in message:
        if info['mimeType'] == 'product':
            return info['layerName']
# print queryPnglayername('a534db7e-637f-4ab1-94d0-e7069a74a5c1', 'tokentest')
# print queryProductLayerName('a534db7e-637f-4ab1-94d0-e7069a74a5c1', 'tokentest')

def queryWMSUrl(metadataid, token = 'tokentest'):
    data = queryData(metadataid)
    if data:
        obj = json.loads(data)
        layerName = queryPnglayername(metadataid, token)
        tllon = obj['upleftLon']
        tllat = obj['upleftLat']
        brlon = obj['lowrightLon']
        brlat = obj['lowrightLat']
        return 'http://%s%s%s&bbox=%f,%f,%f,%f' % (config.IMG_SERVER_HOST, config.IMG_SERVER_WMS_URL, layerName, tllon, tllat, brlon, brlat)
    else:
        config.Log.info("can't get layer wms url, dataid=%s" % metadataid)
        return None
# print queryWMSUrl('085552b2-7565-4906-aeba-3ff8327d7025', 'tokentest')


def queryDataUrl(metadataid, token = '200010035103900'):
    layerName = queryProductLayerName(metadataid, token)
    if layerName:
        return 'info="http://%s%s%s",data="http://%s%s%s"' % (config.IMG_SERVER_HOST, config.IMG_SERVER_INFO_URL, layerName, config.IMG_SERVER_HOST, config.IMG_SERVER_DATA_URL, layerName)
    else:
        return None
# message = queryDataUrl('49c691e5-029f-469a-917c-319e0b955284')
# print message
# print type(message)

# def queryDataUrl(metadataid, token = '200010035103900'):
#     layerName = queryProductLayerName(metadataid, token)
#     if layerName:
#         return 'info="http://%s%s%s",data="http://%s%s%s"' % (config.IMG_SERVER_HOST, config.IMG_SERVER_INFO_URL, layerName, config.IMG_SERVER_HOST, config.IMG_SERVER_DATA_URL, layerName)
#     else:
#         return None
# message = queryDataUrl('013eeae1-c282-418b-a072-17b15e357e53')
# print str(message)
# print type(message)

def uploadFile(fpath, longitude="0.0", latitude="0.0", token="testuser"):
    # config.Log.info('begin upload file: %s' % fpath)
    fsize = os.path.getsize(fpath)
    # print fsize
    if fsize > config.DATA_FILE_SIZE_LIMIT:
        config.Log.info('big file size :%.2fM' % (fsize/1024/1024))
        return None

    url = 'http://%s%s' % (config.DATA_SERVER_HOST, config.DATA_SERVER_UPLOAD_URL)
    try:
        rep = requests.post(url, data={
            "longitude": longitude,
            "latitude": latitude,
            "token": token
        }, files={"file": open(fpath, 'rb')})
        dic = json.loads(rep.content)
        print dic
        return dic
    except:
        print 'false'

# print uploadFile('C:\\Users\\admin\\Desktop\\Metadata.txt')


# def downloadFile(dataid, saveToPath, token=u'testuser'):
#     try:
#         url = 'http://%s%s' % (config.DATA_SERVER_HOST, config.DATA_SERVER_DOWNLOAD_URL)
#         rep = requests.post(url, data = {
#             'id': dataid,
#             'token': token
#         })
#         if rep.status_code != 200:
#             config.Log.info('failed download file (%s:%s)' % (saveToPath, dataid))
#             return
#         with open(saveToPath, 'wb') as f:
#             for data in rep.iter_content(chunk_size = 1024):
#                 f.write(data)
#         config.Log.info('download file success (%s:%s)' % (saveToPath, dataid))
#     except:
#         print 'false'
#         config.Log.info(traceback.format_exc())
#         raise MsgException(ErrorCode.DownloadFaild, u'download file faild. fileid = %s' % dataid)


# def downloadFile(dataid, saveToPath, token=u'testuser'):
#     url = 'http://%s%s' % (config.DATA_SERVER_HOST, config.DATA_SERVER_DOWNLOAD_URL)
#     rep = requests.post(url, data = {
#                                     'id': dataid,
#                                     'token': token
#     })
#     with open(saveToPath, 'wb') as f:
#         for data in rep.iter_content(chunk_size=1024):
#             f.write(data)
#
#
#
# downloadFile('be901fc8-8600-41a1-b98e-766cafd8356e', 'C:\\Users\\admin\\Desktop\\ZY3_TLC_E115.7_N39.8_20130201_L1A0001006160-BWD.rpb')



def listDir(token, dirId):
    try:
        url = 'http://%s%s' % (config.WEBOS_DIR_HOST, config.WEBOS_LISTDIR_URL)
        rep = requests.post(url, {
            'token': token,
            'parentId':dirId
        })
        obj = json.loads(rep.content)

        def _isDir(item):
            return item.get('type') == '1'

        return [{
            'id': item.get('id'),
            'path': item.get('name'),
            'type': 'dir' if _isDir(item) else 'file',
            'metadataid': item.get('metadata')
        } for item in obj['item']['items'] or []]
    except:
        print 'false'
        # config.Log.info(traceback.format_exc())
        # raise MsgException(ErrorCode.ListDirError, u"get dir list error.")

# print listInputDir(token, '200010035338900')
# print listDir(token, '200010035364723')

dirs = '''
[{'path': u'output_e95a581a026b4e94a12e56a6829d7f3a', 'metadataid': None, 'type': 'dir', 'id': 200010035342948L}, {'path': u'output_2b14e8fbaf124d028a3d302e212e102b', 'metadataid': None, 'type': 'dir', 'id': 200010035342881L}, {'path': u'output_b33875485f19442a8efc1d1508d156c8', 'metadataid': None, 'type': 'dir', 'id': 200010035342614L}, {'path': u'output_438a0404597c413e8c507559126dc358', 'metadataid': None, 'type': 'dir', 'id': 200010035342605L}, {'path': u'output_25154546742c4fdcacc50dfed7866051', 'metadataid': None, 'type': 'dir', 'id': 200010035342598L}, {'path': u'output_b186f65eac2a4884a425d2badcb44686', 'metadataid': None, 'type': 'dir', 'id': 200010035342569L}, {'path': u'output_7a4d2dd8c8bc48979b8c2aa9b438597b', 'metadataid': None, 'type': 'dir', 'id': 200010035342570L}, {'path': u'output_31d6f3ad3bce461aac3da4de73f7f7b0', 'metadataid': None, 'type': 'dir', 'id': 200010035342343L}, {'path': u'output_b2be129825b74adaafc0a13b86905b06', 'metadataid': None, 'type': 'dir', 'id': 200010035342040L}, {'path': u'output_3c82a4d1e88e4447aaf015b8e24a9005', 'metadataid': None, 'type': 'dir', 'id': 200010035341633L}, {'path': u'output_f3f7f1fb2e3540ad9a64cd5faf9035a1', 'metadataid': None, 'type': 'dir', 'id': 200010035341493L}, {'path': u'output_6a3d9ed113bc4ef6a31e3fa291d3dd3e', 'metadataid': None, 'type': 'dir', 'id': 200010035341452L}, {'path': u'output_f7e56ea0d8ac465c81753a32ec0e4b83', 'metadataid': None, 'type': 'dir', 'id': 200010035341414L}, {'path': u'output_f0af12c79ddd4508a2b44078f1cee9e8', 'metadataid': None, 'type': 'dir', 'id': 200010035341296L}, {'path': u'output_cbf335246cab412fb32a3cc3a957c0fc', 'metadataid': None, 'type': 'dir', 'id': 200010035341222L}, {'path': u'output_5a95ce58437f43c09b3ca847bff898a9', 'metadataid': None, 'type': 'dir', 'id': 200010035340933L}, {'path': u'output_1de6cfe9d249464d8a8d35325ef2b220', 'metadataid': None, 'type': 'dir', 'id': 200010035340333L}, {'path': u'output_ef1b27d90b5646c0a98797286fed50d1', 'metadataid': None, 'type': 'dir', 'id': 200010035339856L}, {'path': u'output_fd99654954084f79bb60dd38421c2a99', 'metadataid': None, 'type': 'dir', 'id': 200010035339825L}, {'path': u'output_a336e34fcf3144838eccc8795898466c', 'metadataid': None, 'type': 'dir', 'id': 200010035339792L}, {'path': u'output_0b4169f33d254a35ba6f6074cb1ca77a', 'metadataid': None, 'type': 'dir', 'id': 200010035339751L}, {'path': u'output_4ef129d4248643138328ac036d20f36a', 'metadataid': None, 'type': 'dir', 'id': 200010035339711L}, {'path': u'output_c8c4b0541e9b45c0bb999c2fa21981d7', 'metadataid': None, 'type': 'dir', 'id': 200010035339683L}, {'path': u'output_0f45fe4f75e4414e910cb6b42b3b227e', 'metadataid': None, 'type': 'dir', 'id': 200010035339645L}, {'path': u'output_7d5a4e12d7894d45bfb08eb27ea32890', 'metadataid': None, 'type': 'dir', 'id': 200010035339597L}, {'path': u'output_93ee36fff8274f97891de83d05cd1201', 'metadataid': None, 'type': 'dir', 'id': 200010035339572L}, {'path': u'output_3c33f2e1514a42c78f20580f2ab27d58', 'metadataid': None, 'type': 'dir', 'id': 200010035339548L}, {'path': u'output_61256cc7393c4409ae2a8b0cc6a04f30', 'metadataid': None, 'type': 'dir', 'id': 200010035339525L}, {'path': u'output_56d01b25c4314285a0b569659b1dffe5', 'metadataid': None, 'type': 'dir', 'id': 200010035339503L}, {'path': u'output_a9b6c16823e4445884ea52d8977401db', 'metadataid': None, 'type': 'dir', 'id': 200010035339482L}, {'path': u'output_8188cb4019654b3595652121e67e41c0', 'metadataid': None, 'type': 'dir', 'id': 200010035339462L}, {'path': u'output_3c9acf37fd3e40ebb2eedb9a86056632', 'metadataid': None, 'type': 'dir', 'id': 200010035339440L}, {'path': u'output_cc0baa61fa0a4ea48a1aea77a0f26e81', 'metadataid': None, 'type': 'dir', 'id': 200010035339422L}, {'path': u'output_b9d12de6baff4c41b119d8602dcb7fca', 'metadataid': None, 'type': 'dir', 'id': 200010035339405L}, {'path': u'output_4bb98b4f49ba4fe8b96d39d9f766d207', 'metadataid': None, 'type': 'dir', 'id': 200010035339387L}, {'path': u'output_85efa481e95c493483a0a16598303394', 'metadataid': None, 'type': 'dir', 'id': 200010035339370L}, {'path': u'output_bca2f8960bec4c1bbc3a77a234d241e6', 'metadataid': None, 'type': 'dir', 'id': 200010035339356L}, {'path': u'output_0980bef18e8e4d7fbe449f1326bdd676', 'metadataid': None, 'type': 'dir', 'id': 200010035339341L}, {'path': u'output_b91b7d8afcb64d9a9df5a2562b956bd9', 'metadataid': None, 'type': 'dir', 'id': 200010035339307L}, {'path': u'output_a826d47b7afa41179d64e4902707f784', 'metadataid': None, 'type': 'dir', 'id': 200010035339285L}, {'path': u'output_ded6395426104c11b3f26aa52a9ab61f', 'metadataid': None, 'type': 'dir', 'id': 200010035339269L}, {'path': u'output_4d8f56984f8243129405def9a1409020', 'metadataid': None, 'type': 'dir', 'id': 200010035339255L}, {'path': u'output_1260bc47ed534401aeeab8effe90443b', 'metadataid': None, 'type': 'dir', 'id': 200010035339247L}, {'path': u'output_7e0ecc59a53146ccb86b80c280bbe4e7', 'metadataid': None, 'type': 'dir', 'id': 200010035339226L}, {'path': u'output_4d4f97cf435c4857bce3a48efc3089fb', 'metadataid': None, 'type': 'dir', 'id': 200010035339209L}, {'path': u'output_e6d8100d231d4ff5b41dd122501c3fe7', 'metadataid': None, 'type': 'dir', 'id': 200010035339204L}, {'path': u'output_d6c9129e02ec4de2978fab5c8056e1a0', 'metadataid': None, 'type': 'dir', 'id': 200010035338971L}, {'path': u'output_86d82106a6b04498b68bd3803d6b72d5', 'metadataid': None, 'type': 'dir', 'id': 200010035338957L}, {'path': u'output_5c6f8146da03493f8b6adc69a0ad8db9', 'metadataid': None, 'type': 'dir', 'id': 200010035338949L}, {'path': u'output_1e6756767a4044b59cee7bd9b421f82a', 'metadataid': None, 'type': 'dir', 'id': 200010035338946L}, {'path': u'input', 'metadataid': None, 'type': 'dir', 'id': 200010035338901L}]
'''

# def listInputDirByDirid():
#
#     dirid = int('200010035338900')
#
#     def _listdir(dirid):
#         dirs = listDir(token, dirid)
#
#         for d in dirs:
#             if d['type'] == 'dir':
#                 d['children'] = _listdir(d['id'])
#         return dirs
#
#     return flask.jsonify(_listdir(dirid))

# print listInputDirByDirid()




def _listDir(dirid):
    ret = []
    dirs = listDir(token, dirid)
    for d in dirs:
        if d['type'] == 'dir':
            ret.append({
                'type': 'dir',
                'path': d['path'],
                'children': _listDir(d['id'])
            })
        elif d['type'] == 'file':
            obj = {'type': 'file', 'path': d['path']}
            # ft = checkFileType(d['path'])
            # if ft == FileType.TIFF_FILE:
            #     obj['url'] = tiffserver.queryWMSUrl(d['metadataid'], token)
            # elif ft == FileType.SHP_FILE:
            #     obj['url'] = shpserver.queryWMSUrl(d['metadataid'])
            # else:
            #     obj['url'] = dataserver.getPreviewUrl(d['metadataid'])
            ret.append(obj)
    return ret
print _listDir('200010035397000')




