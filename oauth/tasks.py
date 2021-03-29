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


def get_wxapp_userinfo(encrypted_data, iv, code):  # 获取微信用户信息 iv:initialization vector 初始化向量,加密中的随机值
    appid = settings.APPID
    secret = settings.SECRET
    api = WXAPPAPI(appid=appid, app_secret=secret)
    try:
        # 使用 code  换取 session key
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError:
        logger.info(u'OAuth2AuthExchangeError')
        return HttpResponse(status=401)
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(appid, session_key)
    # 解密得到 用户信息
    encrypted_data = str(encrypted_data)
    iv = str(iv)
    user_info = crypt.decrypt(encrypted_data, iv)

    return user_info, session_key


def verify_wxapp(encrypted_data, iv, code):  # 获取openid，注册或返回已有账户 update creat

    user_info, session_key = get_wxapp_userinfo(encrypted_data, iv, code)
    # 获取 openid
    openid = user_info.get('openId', None)
    city = user_info.get('city', None)
    province = user_info.get('province', None)
    avatar = user_info.get('avatarUrl', None)
    if openid:
        auth, created = UserInfo.objects.update_or_create(openid=openid,
                                                           defaults={
                                                                     "avatar": avatar, "city": city,
                                                                     "province": province, "session_key": session_key})
        return auth
    # auth is an object
    return False