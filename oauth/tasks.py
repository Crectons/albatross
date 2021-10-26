from django.http import HttpResponse
from django.conf import settings

from weixin.lib.wxcrypt import WXBizDataCrypt
from weixin import WXAPPAPI
from weixin.oauth2 import OAuth2AuthExchangeError

from server.models import UserInfo

import hmac
import struct
import hashlib
import time
import base64
import requests
import json
import random
import logging

logger = logging.getLogger(__name__)


def get_wxmp_openid(code):  # 获取微信用户信息 iv:initialization vector 初始化向量,加密中的随机值
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


def verify_wxapp(encrypted_data, iv, code):  # 获取openid，注册或返回已有账户 update creat

    # 获取 openid
    openid = get_wxmp_openid(code)
    if openid:
        auth, created = UserInfo.objects.update_or_create(openid=openid,
                                                           defaults={})
        return auth
    # auth is an object
    return False