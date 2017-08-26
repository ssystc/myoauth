#coding=utf-8

import config
import requests
import json
import traceback

req = requests.get('http://192.168.4.3:8808/metadata-service/metadata/manage/id?id=5a070950-3f77-4c02-9ca1-3c49a3c4657c&token=ogqDmSTZ1/KSasSwrZh6u51cTlzs1A/dKAcsXzy/jw4cTH1NXIOrXf95L8WZe57qOiiGeyjDGtS4wIwQ7CfQeNfQblMcIFMjSwnTg/TrszLNE0I4UQBrb7Dc2ZsGIsQv7ptQin2pAVZa1Vvtv5dVd2Ugo0bWF7oW0WHi+/at8Qw=')
print req.content