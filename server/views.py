from django.shortcuts import render
import hashlib
import json

from django.http import HttpResponse, JsonResponse
# from django.core import serializers
from oauth.utils import verify_request
from weixin.lib.wxcrypt import WXBizDataCrypt

from server.tasks import *

def test(request):
    return HttpResponse(status=200)

def photo(request): #图片上传服务
    return HttpResponse(status=200)