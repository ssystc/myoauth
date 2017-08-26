# coding: utf-8

import urllib2
from poster.streaminghttp import register_openers
from poster.encode import multipart_encode
import json
import config
import os
import subprocess

import traceback

import requests


def queryData(dataid):
    url = 'http://%s%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_QUERY_URL, str(dataid))
    try:
        rep = requests.get(url)
        return rep.content
    except:
        config.Log.info(traceback.format_exc())
        return None

queryData('e0fa8dd8-02bc-4259-848d-86d195d9c139')


def queryLayerName(dataid):
    data = queryData(dataid)
    if data:
        obj = json.loads(data)
        return obj["layerName"]
    else:
        config.Log.info("can't get layer name, dataid=%s" % dataid)
        return None


def queryWMSUrl(dataid):
    data = queryData(dataid)
    if data:
        obj = json.loads(data)
        layerName = obj["layerName"]
        tllon = obj['upleftLon']
        tllat = obj['upleftLat']
        brlon = obj['lowrightLon']
        brlat = obj['lowrightLat']
        return 'http://%s%s%s&bbox=%f,%f,%f,%f' % (
        config.IMG_SERVER_HOST, config.IMG_SERVER_WMS_URL, layerName, tllon, tllat, brlon, brlat)
    else:
        config.Log.info("can't get layer wms url, dataid=%s" % dataid)
        return None


# 可以让支持netimg格式的gdal访问的url
def queryDataUrl(dataid):
    layerName = queryLayerName(dataid)
    if layerName:
        return 'info="http://%s%s%s",data="http://%s%s%s"' % (
        config.IMG_SERVER_HOST, config.IMG_SERVER_INFO_URL, layerName, config.IMG_SERVER_HOST,
        config.IMG_SERVER_DATA_URL, layerName)
    else:
        return None

print queryDataUrl('807f3f5c-374f-41d1-93a8-34a6d30fa769')


def uploadTiffFile(fpath, isDem=0):
    config.Log.info('begin upload tiff file: %s' % fpath)

    def _transSpimgToTiff(fpath):
        spdatapath = fpath + '.data'
        if os.path.isdir(spdatapath):
            tiffpath = fpath + '.tiff'
            config.Log.info('convert spimg to tiff <%s:%s>' % (fpath, tiffpath))
            # subprocess.call("gdal_translate %s %s" % (fpath, tiffpath), shell=True)
            subprocess.call("bash ./common/trans/trans.sh %s %s GTiff" % (fpath, tiffpath), shell=True)
            return tiffpath
        return fpath

    try:
        tiffpath = _transSpimgToTiff(fpath)

        register_openers()
        datagen, headers = multipart_encode({"file": open(tiffpath, "rb"),
                                             "imageMeta.isDem": isDem,
                                             "imageMeta.tileType": 1
                                             })

        url = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_DATA_UPLOAD_URL)
        req = urllib2.Request(url, datagen, headers)

        if tiffpath != fpath:
            os.remove(tiffpath)

        message = urllib2.urlopen(req).read()
        obj = json.loads(message)

        return obj['id']
    except:
        config.Log.info(traceback.format_exc())
        raise MsgException(ErrorCode.UploadTiffFileFaild, u'upload tiff file faild. path = %s' % fpath)


def isSpimgPertian(fpath):
    if fpath.endswith('.data'):
        tifPath = fpath[0:len(fpath) - 5]
        if os.path.exists(tifPath) and os.path.isfile(tifPath):
            return True
    return False