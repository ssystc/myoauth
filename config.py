#coding=utf-8

PRIVATE_KEY="""-----BEGIN PRIVATE KEY-----
                MIICXQIBAAKBgQDf3qWLHkHBVC3AW/ch/dut5pd39E2L7l6cJ0QK/hOE9VCue8DAm0mw42631zRib38uhnG5UjYfUd4CHKPlje/RiIEni+/ihwcY7pNtIKLMgUcTXe4Ve7TTznlmG9R/Rvse5x5vqfRVVKMNturSlLE2nQRB8HfTv38r/l2pnGG8gQIDAQABAoGBAMKvG+Wk1WgsLXFoSL2dx4ouyzB9G2cCT/KaTxkEJbNtptFmO5UENoyG7IUhuKOV9NNgBcw1C24nQtsxTvLVgWRlMRmIjsJZnHw6qZ7Tv6NhtsDhmccfDzciZ36mR5hjssDpAqECVKzR4AGdssf191QDUHApQdHF2haN5UOVXO3FAkEA9rT59Kafj8iZZr2lNsBZ0/xBW+4C27ri+338Yi8F+vEO2ws+aktaREvoPxd3WbKBadO4zfxG98+djRoERgUBxwJBAOhNcsCfahHPK403h2Do/xMsmNNsDCKQd+cUeO5Nax/H+hVbaBkU4/uLVGP5gtXqRllTx9GgTTD93me5ef9yz3cCQD20tnBC3NYRzoysEo7HPbCP/6kGtyBOdkeBE4dbS5ugf566CTp87m72rXhaXjfJNiVKF4ct+nIxM67/OuJojjECQHvOSwo969nx/9QTdCNCCi+95PVI8G67cCvHzWuz9xPJEI+xV5mGeLrnVuKxZ/l6EmQpMqWWOY2Sv6WoREzQc6ECQQC9guI3RcL3n41bfF8FgxsLIBh+VYu00GPV557UHoq3Uc3xbhDFBhauS/rFrkjM3adATCnWximl/KY6dG/X3Vmk
                -----END PRIVATE KEY-----"""


PUBLIC_KEY='''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDf3qWLHkHBVC3AW/ch/dut5pd3
9E2L7l6cJ0QK/hOE9VCue8DAm0mw42631zRib38uhnG5UjYfUd4CHKPlje/RiIEn
i+/ihwcY7pNtIKLMgUcTXe4Ve7TTznlmG9R/Rvse5x5vqfRVVKMNturSlLE2nQRB
8HfTv38r/l2pnGG8gQIDAQAB
-----END PUBLIC KEY-----'''


SECRET_KEY='asdfasdfvasg'





WEB_SERVER_IP='127.0.0.1'
WEB_SERVER_PORT=8888

# CLIENT_ID = '200010035116400'
# OAUTH_URL='192.168.4.225:8443'
# OAUTH_LOGIN_URL='/user_oauth/oauth-server-idp/oauth2/authorize?client_id=%s&redirect_uri=%s%s&response_type=token'
# OAUTH_VARIFY_URL='/user_oauth/oauth-server-idp/verify2'
# OAUTH_REDIRECT_URL='http://127.0.0.1:8888/user/logincallback/'


CLIENT_ID = '200010035326904'
OAUTH_URL = '192.168.4.225:8443'
OAUTH_LOGIN_URL = '/user_oauth/oauth-server-idp/oauth2/authorize?client_id=%s&redirect_uri=%s%s&response_type=code'
OAUTH_REQUIRE_TOKEN_URL = '/user_oauth/oauth-server-idp/oauth2/access_token'
OAUTH_VARIFY_URL = '/user_oauth/oauth-server-idp/verify2'
OAUTH_REDIRECT_URL = 'http://%s:%s/user/logincallback/' % (WEB_SERVER_IP, WEB_SERVER_PORT)
INDEX_PAGE = '/pixelfactory/views/task/pixelfactory.html'

DB_ADDRESS = 'postgresql://postgres:123456@127.0.0.1:5432/testbase'
Log = None




WEBOS_DIR_HOST = '192.168.44.5:8080'
WEBOS_MKDIR_URL = '/user_data/favorites/addFavoritesInfo'
WEBOS_LISTDIR_URL = '/user_data/favorites/getFavoritesinfobyParentID'
WEBOS_EDITOR_URL = '/user_data/favorites/editFavoritesInfo'


# 张卓上传文件以及根据id查询接口
TIFF_DATA_HOST = '192.168.4.3:8808'
TIFF_DATA_UPLOAD_URL = '/image-service/manager/uploadImage.action'
TIFF_DATA_QUERY_BY_METAID = '/metadata-service/metadata/manage/id'
TIFF_DATA_QUERY_BY_TIFFID = '/image-service/image/query/id'
TIFF_QUERY_SLICE_URL = '/image-service/image/query/getTileServer'


SHP_SERVER_HOST = '192.168.4.229:8509'
SHP_SERVER_UPLOAD_URL = '/uploadFiles'
SHP_WMS_HOST = '192.168.4.229:28080'
SHP_WMS_URL = '/Liu0821Upload/SearchWMS'



DATA_SERVER_HOST = '192.168.4.221:8670'
DATA_SERVER_UPLOAD_URL = '/fileManagement/upload'
DATA_SERVER_DOWNLOAD_URL = '/fileManagement/Download'
DATA_FILE_SIZE_LIMIT = 10 * 1024 * 1024



IMG_SERVER_HOST = '192.168.4.3:18080'
IMG_SERVER_WMS_URL = '/geowebcache/service/wms?TIMESTAMP=2012-05-29%2009:45:35.0&QUERYTYPE=phasetile&service=WMS&request=GetMap&version=1.1.1&layers='
IMG_SERVER_INFO_URL = '/geowebcache/product/getinfo?productid='
IMG_SERVER_DATA_URL = '/geowebcache/product/tile?layers='
