# Create your views here.
# -*- coding: UTF-8 -*-
import time
import jwt
from django.http import HttpResponse, JsonResponse
from oauth.tasks import *
import logging
import json
import requests
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.header import Header

logger = logging.getLogger(__name__)


def oauth(request):
    if request.method == "POST":
        req = json.loads(request.body.decode())
        ed = req.get('ed')  # encrypted_data
        iv = req.get('iv')  # initialization vector
        code = req.get('code')  # code
        logger.info(u'Received request successfully')
        account = verify_wxapp(ed, iv, code)  # 此步进行数据库的存储或更新

        if not account:
            response = {}
            response.status_code = 406
            response['message'] = "获取openid失败"
            logger.info(u'Failed getting openid.')
            return response
        logger.info(u'Got openid successfully')

        return JsonResponse({'uid': account.uid})
