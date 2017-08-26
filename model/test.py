# coding: utf-8

import requests
import config
import json
import webserver.user
from model.logininfo import LoginInfoDao
import M2Crypto
import base64
from model.stateclan import StateClanDao, StateClan

# list = LoginInfoDao.querytokenByusername('yw', '200010035116700')
# for info in list:
#     print info.token

stateclanList = StateClanDao.queryByTaskId('6e02fa4bda34432a902133c451a32305', '200010035324693')
print stateclanList