import logging
from django.http import HttpResponse
from django.conf import settings
from albatross.libs.weixin.client import WeixinMpAPI
from albatross.libs.weixin import WXAPPAPI
from albatross.libs.weixin.oauth2 import OAuth2AuthExchangeError


logger = logging.getLogger('django')


def get_wxmp_openid(code):
    """
    公众号平台登录
    获取微信用户信息 iv:initialization vector 初始化向量, 加密中的随机值
    """
    appid = settings.APPID
    secret = settings.SECRET
    api = WXAPPAPI(appid=appid, app_secret=secret)
    try:
        # 使用 code  换取 session_info
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError:
        logger.info(u'OAuth2AuthExchangeError')
        return HttpResponse(status=401)
    openid = session_info.get('openid')
    return openid


def get_wxweb_openid(code):
    """
    web 端登录
    """
    appid = settings.APPID
    secret = settings.SECRET
    # scope = ('snsapi_base',)
    api = WeixinMpAPI(appid=appid, app_secret=secret)
    try:
        access_info = api.exchange_code_for_access_token(code=code)
        # 使用 code  换取 session_info
    except OAuth2AuthExchangeError:
        logger.info(u'OAuth2AuthExchangeError')
        return HttpResponse(status=401)
    openid = access_info.get('openid')
    return openid
