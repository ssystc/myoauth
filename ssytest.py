#coding=utf-8
import requests
import flask.sessions
import json
import config


# def test(a):
#     def _mytest():
#         print a
#
#     _mytest()
# test('dagasgf')


# osdirs = {}
# a = {}
# d = { 'id': '1',
#       'path': 'ssypath',
#       'type': 'dir',
#       'metadataid': 'dsafqwfdsaf'}
# osdirs['ssypath'] = d
# a['key'] = 'value'
# a['bbb'] = 'bbb'
# print osdirs
# print a
# print a['key']




# rep = requests.post('http://192.168.4.221:8283/api/task/start', data={'id': 'be0b88ed1aaf41efb68d227fe7ced656'})
# print rep.content

# rep = requests.post('http://192.168.4.221:8283/api/taskstatus/query', data={'flowid': 'f1f4189f0e6745f8bf93d226cdfcf0e9'})
# print rep.content

rep = requests.post('http://192.168.4.221:8283/api/stateclan/query', data={'taskid': '907781a34d074477ae4b5c3566918e94'})
print rep.content

# rep = requests.post('http://192.168.4.221:8283/api/fs/listinput', data={'dirid': '200010035345400'})
# print rep.status_code
# print rep.content



# mylist = ['a', 'b', 'c']
# mylist.pop(1)
# print mylist

# token = 'P6Aeeg48OD9ncrulH63ZLPfNco5JLDsaa1cV2Dz7KZco6iN4W/bzvJHMMfFKSqFVEc7BYPEqo9J+C9nPjSd6YEaWd9ugeZ1vWBAtP8/ma6397WYIW+n9UpGXSE691pIoE7g42wpa0I68sWOsANkQu522IrKpqQG8m/RX6k60ZKI='


# def listDirByDirid():
#     userid = '200010035116700'
#     token = 'P6Aeeg48OD9ncrulH63ZLPfNco5JLDsaa1cV2Dz7KZco6iN4W/bzvJHMMfFKSqFVEc7BYPEqo9J+C9nPjSd6YEaWd9ugeZ1vWBAtP8/ma6397WYIW+n9UpGXSE691pIoE7g42wpa0I68sWOsANkQu522IrKpqQG8m/RX6k60ZKI='
#     dirid = int('200010035338901')
#
#     def _listdir(dirid):
#         dirs = listDir(token, dirid)
#         for d in dirs:
#             if d['type'] == 'dir':
#                 d['children'] = _listdir(d['id'])
#         return dirs
#
#     return flask.jsonify(_listdir(dirid))
#
#
# def listDir(token, dirId):
#     try:
#         url = 'http://%s%s' % (config.WEBOS_DIR_HOST, config.WEBOS_LISTDIR_URL)
#         rep = requests.post(url, {
#             'token': token,
#             'parentId':dirId
#         })
#         obj = json.loads(rep.content)
#
#         def _isDir(item):
#             return item.get('type') == '1'
#
#         return [{
#             'id': item.get('id'),
#             'path': item.get('name'),
#             'type': 'dir' if _isDir(item) else 'file',
#             'metadataid': item.get('metadata')
#         } for item in obj['item']['items'] or []]
#     except:
#         print 'false'
#
# print listDir(token,int('200010035338901'))

# print listDirByDirid()


# params = [{
#         "auto": ["dir_mss", "dir_pan"],
#         "mulit": False
#     },
#     {
#         "auto": ["_BundleAdj.rpb", "_RPC.rpb", "dir_mss", "dir_pan"],
#         "mulit": False
#     }]
#
# print params
# del params[:]
# print params


# test = ['a', 'b', 'c', 'd']
# test.pop(0)



# inputfiles = [
#     {
#         "index": 0,
#         "multi": True,
#         "name": "InputImgFileName",
#         "title": "panimg",
#         "type": "url",
#         "value": "info=\"http://192.168.4.221:9090/geowebcache/product/getinfo?productid=GF2_PMS1_E113.6_N40.3_20160308_L1A0001458078-PAN1_1013_product\",data=\"http://192.168.4.221:9090/geowebcache/product/tile?layers=GF2_PMS1_E113.6_N40.3_20160308_L1A0001458078-PAN1_1013_product\""
#     },
#     {
#         "index": 1,
#         "multi": True,
#         "name": "InputImgFileName",
#         "title": "panimg",
#         "type": "url",
#         "value": "info=\"http://192.168.4.221:9090/geowebcache/product/getinfo?productid=GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-PAN1_1014_product\",data=\"http://192.168.4.221:9090/geowebcache/product/tile?layers=GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-PAN1_1014_product\""
#     },
#     {
#         "index": 0,
#         "multi": True,
#         "name": "InputRPCFileName",
#         "title": "panrpb",
#         "type": "url",
#         "value": "/data/llts-data/pf2/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/input/pan/GF2_PMS1_E113.6_N40.3_20160308_L1A0001458078-PAN1/GF2_PMS1_E113.6_N40.3_20160308_L1A0001458078-PAN1.rpb"
#     },
#     {
#         "index": 1,
#         "multi": True,
#         "name": "InputRPCFileName",
#         "title": "panrpb",
#         "type": "url",
#         "value": "/data/llts-data/pf2/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/input/pan/GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-PAN1/GF2_PMS1_E113.6_N40.1_20160308_L1A0001458090-PAN1.rpb"
#     }
#
# ]
# print inputfiles
# def __reset(params):
#     name2Obj = {}
#
#     print params
#
#     for inp in params:
#         name2Obj[inp['name']] = inp
#
#     print name2Obj
#
#     del params[:]
#     print params
#
#     for inp in name2Obj.itervalues():
#         print inp.get('multi')
#         if inp.get('multi'):
#             print ''
#             inp.pop('index')
#         params.append(inp)
#     return params
# print __reset(inputfiles)

# list = [1,2,3,4,5]
#
# for i in list:
#     if i == 3:
#         state = 'True'
#         break
#     else:
#         state = 'Fales'
#
# print state

# state = {
#             'paused':1,
#             'state': 2 ,
#             'errorCode': 3,
#             'errorMessage': 4,
#             'fileuploading': False
#          }
# modules = {
#     'amodule': {'uploading': True,'finished':False},
#     'bmodule': {'uploading': True,'finished':False}
#
# }



# class module(object):
#     def __init__(self,code, uploading):
#         self.code = code
#         self.uploading = uploading
#
# startmodule = module(0, True)
# endmodule  = module(0, False)
#
# modules = {
#     'startmodule': startmodule,
#     'endmodule':endmodule
# }
#
# def getState():
#     for name, module in modules.items():
#         if module.uploading == True:
#             state = {
#                 'state': 2 ,
#                 'fileuploading': True
#             }
#             break
#         else:
#             state = {
#                 'state': 2 ,
#                 'fileuploading': False
#             }
#
#     for name, module in modules.items():
#         moduleState = {
#             'code': module.code,
#             'uploading': module.uploading
#         }
#         state[name] = moduleState
#     return state
#
# print getState()

# testlist = []
# jsontest = json.dumps(testlist)
# print jsontest
# if jsontest:
#     print 'not none'
# else:
#     print 'none'

# clan = {
#     'a': 1,
#     'b':2
# }
#
# time ={
#     'starttime': 111,
#     'endtime':222
# }
#
# all = time + clan









