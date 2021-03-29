# jwt token已在新版本取消，取代的是自强API的token
import json
from functools import wraps

import requests
from django.http import HttpResponse, JsonResponse
from oauth.tasks import *

def get_error_info(dic):
    error_message = dic.get("error")
    mp = {"invalid_request": "参数格式 / 请求流程非法", "invalid_grant": "密码 / 验证码错误",
          "invalid_token": "携带了无效的Token", "expired_token": "携带了过期的token",
          "permission_denied": "携带的 Token 无权访问此接口", "no_authorization": "未提供 Token", }
    return mp.get(error_message)


def verify_request(func):
    def wrapper(request, *args, **kwargs):
        '''
        token=request.GET.get('token')
        status_code,text=ZQ_API.verify_token(token)
        dic = json.loads(text)
        if status_code == 200:
            if dic.get("expires_in") == -1:
                return JsonResponse({"status_code": 401, "message": "携带了过期的token"})
            elif dic.get("permissions")["information"]:
                return func(request, *args, **kwargs)
            else:
                return JsonResponse({"status_code": 403, "message": "token无信息门户权限"})
        else:
            return JsonResponse({"status_code": status_code, "message": get_error_info(dic)})
        '''
        return func(request, *args, **kwargs)
    return wrapper

"""
import jwt
from django.http import JsonResponse


def get_authorization(request):  # 区分Auth类型，获取jwt_token自定义登录态
    authorization = request.headers.get('Authorization')
    if not authorization:
        return False, None
    try:
        authorization_type, token = authorization.split(' ')
        return authorization_type, token
    except ValueError:
        return False, None

def verify_jwt_token(token):
    from jwt.exceptions import ExpiredSignatureError
    try:
        payload = jwt.decode(token, 'secret',
                             audience="vx",
                             algorithms=['HS256'])
    except ExpiredSignatureError:
        return False, token
    if payload:
        return True, payload["sub"]
    return False, token

def verify_request(func):  # 请求时鉴权

    def wrap(request):
        authorization_type, token = get_authorization(request)
        if authorization_type == 'JWT':
            status, id_num = verify_jwt_token(token)
            if status:
                return func(request, id_num)
            else:
                return JsonResponse({"message":"无效请求：权限验证不通过"})
        return False, None

    return wrap
"""
