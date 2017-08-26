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

'http://192.168.4.3:8808/image-service/image/query/getTileServer'
url = 'http://%s%s' % (config.TIFF_DATA_HOST, config.TIFF_QUERY_SLICE_URL)
token = 'JsmHbozbhoVIO7f9I5Xp2qw2E+DmqeaK5bNCNZVoSe7Zz4e2T0fDUL8nlCQxC1BZHkLwI5VH0m/TtByDSGSckY3XdQTnaBxhQlVmiNfLuRkYUT5DGDJXpOPUaSVtwc04o+TTbtNoy+ZShLOFg0nnmHiCIdQv5u84nAEuu1aN7Ng='

rep = requests.get('http://%s%s/?token=%s' % (config.TIFF_DATA_HOST, config.TIFF_QUERY_SLICE_URL, token))





print rep.content

# rep = requests.post('http://192.168.4.3:8808/image-service/image/manage/getTileserver')
# print rep.content