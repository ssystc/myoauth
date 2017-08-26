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

token = 'rBkifGOF9rR3CzSCc+tTAkSCPcRXmEsdlitJEHNNzqhfhZEqJWQDh2HgxGrMSfvfhqsCOyzHqCA9zQeUe4/Pm+z8jiQtVoQy3xcwa9/0/SK9dpStpevpUYns+jRPPKqCNVsAIslZ0P13fhFAdCq5mXfRtE/sBHhCXEH45AHvDso='

#上传Tiff文件接口
# def uploadTifFile(file,isDem=0):
#     register_openers()
#     datagen, headers = multipart_encode({"file": open(file, "rb"),
#                                          "imageMeta.isDem": isDem
#                                          })
#     req=urllib2.Request('http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_UPLOAD_URL), datagen, headers)
#     message=urllib2.urlopen(req).read()
#     mydic = json.loads(message,encoding="utf-8")
#     metadataId = mydic['metadataId']
#     tiffId = mydic['id']
#
#     return metadataId, tiffId
#
# metadata, tiffId = uploadTifFile("C:\\Users\\admin\\Desktop\\123.tif")
# print metadata
# print tiffId



# def uploadTiffFile(fpath, mimetypes, token, isBase =0 ,isDem = 0):
#     # config.Log.info('begin upload tiff file: %s' % fpath)
#     #
#     # def _transSpimgToTiff(fpath):
#     #     spdatapath = fpath + '.data'
#     #     if os.path.isdir(spdatapath):
#     #         tiffpath = fpath + '.tiff'
#     #         config.Log.info('convert spimg to tiff <%s:%s>' % (fpath, tiffpath))
#     #         # subprocess.call("gdal_translate %s %s" % (fpath, tiffpath), shell=True)
#     #         subprocess.call("bash ./common/trans/trans.sh %s %s GTiff" % (fpath, tiffpath), shell=True)
#     #         return tiffpath
#     #     return fpath
#
#
#     register_openers()
#     datagen, headers = multipart_encode({"file": open(fpath, "rb"),
#                                              "imageMeta.isDem": isDem,
#                                              "imageMeta.isBase": isBase,
#                                              "mimeTypes": mimetypes,
#                                              'token': token
#                                         })
#
#     url = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_UPLOAD_URL)
#     req = urllib2.Request(url, datagen, headers)
#
#         # if tiffpath != fpath:
#         #     os.remove(tiffpath)
#
#     message = urllib2.urlopen(req).read()
#     # code = urllib2.urlopen(req).getcode()
#     # return message
#     # print code
#     # return code
#     # print message
#     obj = json.loads(message)
#
#     return obj['metadataId']
#
#         # config.Log.info(traceback.format_exc())
#         # raise MsgException(ErrorCode.UploadTiffFileFaild, u'upload tiff file faild. path = %s' % fpath)

# print uploadTiffFile("C:\\Users\\admin\\Desktop\\1234.tiff", json.dumps(['png', 'product']), token)


def uploadTiffFile(fpath, mimetypes, token, isBase =0 ,isDem = 0):
    # config.Log.info('begin upload tiff file: %s' % fpath)

    # def _transSpimgToTiff(fpath):
    #     spdatapath = fpath + '.data'
    #     if os.path.isdir(spdatapath):
    #         tiffpath = fpath + '.tiff'
    #         config.Log.info('convert spimg to tiff <%s:%s>' % (fpath, tiffpath))
    #         # subprocess.call("gdal_translate %s %s" % (fpath, tiffpath), shell=True)
    #         subprocess.call("bash ./common/trans/trans.sh %s %s GTiff" % (fpath, tiffpath), shell=True)
    #         return tiffpath
    #     return fpath

    try:
        # tiffpath = _transSpimgToTiff(fpath)

        register_openers()
        datagen, headers = multipart_encode({"file": open(fpath, "rb"),
                                             "imageMeta.isDem": isDem,
                                             "imageMeta.isBase": isBase,
                                             "mimeTypes": mimetypes,
                                             'token': token
                                            })

        url = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_UPLOAD_URL)
        req = urllib2.Request(url, datagen, headers)

        # if tiffpath != fpath:
        #     os.remove(tiffpath)

        message = urllib2.urlopen(req).read()

        print message

        obj = json.loads(message)
        print obj
        return obj['metadataId']
    except:
        print traceback.format_exc()
        # config.Log.info(traceback.format_exc())
        # raise MsgException(ErrorCode.UploadTiffFileFaild, u'upload tiff file faild. path = %s' % fpath)

print uploadTiffFile("C:\\Users\\admin\\Desktop\\1234.tiff", json.dumps(['png', 'product']), token)