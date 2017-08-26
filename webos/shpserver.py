# coding: utf-8

import zipfile
import os
import traceback
import urllib2
import time
import config
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode
import requests
import json
import uuid


path = 'C:\\Users\\admin\\Desktop\\shpserver_test\\ssy.shp'


def getShpExt():
    return ['.dbf', '.prj', '.shx']

def isShpPertain(fpath):
    exts = set(getShpExt())
    name, ext = os.path.splitext(fpath)
    ext = ext.lower()
    if ext in exts and os.path.exists(name + '.shp'):
        return True
    return False

def zipShpFile(fpath):
    if not os.path.exists(fpath):
        return None

    try:
        filename = os.path.splitext(fpath)[0]           #C://test//testshp

        layername = uuid.uuid4()                     #dafasdf
        dirname = os.path.dirname(filename)
        newfilename = '%s\\%s' % (dirname, layername)      #C://test//dasfgasdfasd


        zfpath = '%s%s' % (newfilename, '.zip')         #C://test//dafasdf.zip

        ach = os.path.basename(filename)                #testshp

        zf = zipfile.ZipFile(zfpath, 'w')
        zf.write(fpath, ('%sshp' % layername))

        print fpath


        for fext in getShpExt():
            fname = '%s%s' % (filename, fext)
            if os.path.exists(fname):
                zf.write(fname, ('%s%s' % (layername, fext)))
        zf.close()

    except:
        config.Log.info(traceback.format_exc())
        config.Log.info('upload shp file error.')
        return None
    finally:
        # print 'end'
        print zfpath
        if zf:
            zf.close()
        # if zfpath and os.path.exists(zfpath):
        #     os.remove(zfpath)

# zipShpFile('C:\\Users\\admin\\Desktop\\shpserver_test\\liutestshp.shp')



def onlyUpload(fpath):

    register_openers()
    datagen, headers = multipart_encode({"vector": open(fpath, "rb"),
                                         "name": "ssy",
                                         "vector_desc": "ssytest",
                                         "scale": "5w",
                                         "charset": "GBK",
                                         "product_time": time.time(),
                                         "type": "SHP",
                                         "ref_srs": "EPSG:4326"
                                        })

    url = 'http://%s%s' % (config.SHP_SERVER_HOST,
                            config.SHP_SERVER_UPLOAD_URL)
    req = urllib2.Request(url, datagen, headers)

    message = urllib2.urlopen(req).read()
    message = json.loads(message)
    dataid = message['uuid']
    return dataid

# print onlyUpload('C:\\Users\\admin\\Desktop\\shpserver_test\\pacific0.zip')


# def uploadShpFile(fpath):
#     if not os.path.exists(fpath):
#         return None
#
#     try:
#         layername = uuid.uuid4()
#         filename = os.path.splitext(fpath)[0]
#         print filename
#
#         dirname = os.path.dirname(filename)
#         newfilename = '%s\\%s' % (dirname, uuid.uuid4())
#         print newfilename
#
#
#         zfpath = '%s%s' % (filename, '.zip')
#         print zfpath
#
#         ach = os.path.basename(filename)
#         print ach
#
#         zf = zipfile.ZipFile(zfpath, 'w')
#         zf.write(fpath, os.path.join(ach, os.path.basename(fpath)))
#
#
#
#
#         for fext in getShpExt():
#             fname = '%s%s' % (filename, fext)
#             if os.path.exists(fname):
#                 zf.write(fname, os.path.join(ach, os.path.basename(fname)))
#         zf.close()
#
#
#         register_openers()
#         f = open(zfpath, "rb")
#         datagen, headers = multipart_encode({"vector": f,
#                                              "name": "ssy",
#                                              "vector_desc": "ssytest",
#                                              "scale": "5w",
#                                              "charset": "GBK",
#                                              "product_time": time.time(),
#                                              "type": "SHP",
#                                              "ref_srs": "EPSG:4326"
#                                              })
#
#         url = 'http://%s%s' % (config.SHP_SERVER_HOST,
#                                 config.SHP_SERVER_UPLOAD_URL)
#         req = urllib2.Request(url, datagen, headers)
#
#         message = urllib2.urlopen(req).read()
#         jsonmessage = json.loads(message)
#         dataid = jsonmessage['uuid']
#         return dataid
#     except:
#         # print 'error'
#         config.Log.info(traceback.format_exc())
#         config.Log.info('upload shp file error.')
#         return None
#     finally:
#         # print 'end'
#         if zf:
#             zf.close()
#         # if zfpath and os.path.exists(zfpath):
#         #     f.close()
#         #     os.remove(zfpath)

# print uploadShpFile('C:\\Users\\admin\\Desktop\\shpserver_test\\liutestshp.shp')

# zfpath = 'C:\\Users\\admin\\Desktop\\shpserver_test\\liutestshp.zip'
# os.remove(zfpath)


mystr = '''
{"map_extent": "POLYGON((107.140093 34.371773,107.140093 34.377808,107.156785 34.377808,107.156785 34.371773,107.140093 34.371773))", "group_uuid": "", "vector_desc": "ssytest", "vec_style_uuid": "", "ref_srs": "EPSG:4326", "thumbnail_path": "", "name": "ssy", "user_id": "123", "uuid": "cf8649ee-b95e-4dee-b456-2082865b5594", "product_time": "1503048275.96", "dtTable": "vt_ssy_liu_testshp_v01", "save_path": "/home/temp/liutestshp.zip", "load_time": "2017-08-19 16:22:53", "type": "SHP"}
'''
# f = open('C:\\Users\\admin\\Desktop\\shpserver_test\\liutestshp.zip')
# f.close()
# os.remove('C:\\Users\\admin\\Desktop\\shpserver_test\\liutestshp.zip')


# filename = 'C:\\Users\\admin\\Desktop\\shpserver_test\\liutestshp'
# filename = os.path.dirname(filename)
# newfilename = '%s\\%s' % (filename, uuid.uuid4())
# print newfilename




def uploadShpFile(fpath):
    if not os.path.exists(fpath):
        return None

    try:
        filename = os.path.splitext(fpath)[0]

        layername = uuid.uuid4()
        dirname = os.path.dirname(filename)
        newfilename = '%s\\%s' % (dirname, layername)

        zfpath = '%s%s' % (newfilename, '.zip')

        zf = zipfile.ZipFile(zfpath, 'w')
        zf.write(fpath, ('%sshp' % layername))

        for fext in getShpExt():
            fname = '%s%s' % (filename, fext)
            if os.path.exists(fname):
                zf.write(fname, ('%s%s' % (layername, fext)))
        zf.close()

        register_openers()
        f = open(zfpath, "rb")
        datagen, headers = multipart_encode({"vector": f,
                                             "name": "ssy",
                                             "vector_desc": "ssytest",
                                             "scale": "5w",
                                             "charset": "GBK",
                                             "product_time": time.time(),
                                             "type": "SHP",
                                             "ref_srs": "EPSG:4326"
                                             })

        url = 'http://%s%s' % (config.SHP_SERVER_HOST,
                               config.SHP_SERVER_UPLOAD_URL)
        req = urllib2.Request(url, datagen, headers)

        message = urllib2.urlopen(req).read()
        message = json.loads(message)
        dataid = message['uuid']
        return dataid
    except:
        print traceback.format_exc()
        # config.Log.info(traceback.format_exc())
        # config.Log.info('upload shp file error.')
        # return None
    finally:
        if zf:
            zf.close()
        if zfpath and os.path.exists(zfpath):
            f.close()
            os.remove(zfpath)

# print uploadShpFile('C:\\Users\\admin\\Desktop\\shpserver_test\\liutestshp.shp')



dataid = '7f953cfc-fd29-4a01-bcc0-5cd60c192b02'
def queryWMSUrl(metadataid):
    try:
        url = 'http://%s%s?uuid=%s' % (config.SHP_WMS_HOST, config.SHP_WMS_URL, metadataid)
        rep = requests.get(url)
        message = json.loads(rep.content)
        return message['png']
    except:
        config.Log.info(traceback.format_exc())
        config.Log.info("can't get shp wms url, metadataid = %s" % metadataid)
        return None
print queryWMSUrl(dataid)
# message = json.loads(req.content)
# print message






