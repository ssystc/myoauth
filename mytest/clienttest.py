#coding=utf-8

import requests

rep=requests.get('http://127.0.0.1:8888/')
print rep.text

