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
    logger.info(u'Got request successfully with method {sid}.'.format(sid=request.method))
    
    if request.method == "GET":
        code = request.GET.get('code')  # code
        type = request.GET.get('type')  # type
        logger.info(u'Received request successfully')
        if (type == 'mp'):
            account = verify_wxmp(code)  # 此步进行数据库的存储或更新
        elif (type == 'web'):
            account = verify_wxweb(code)  # 此步进行数据库的存储或更新

        if not account:
            response = {}
            response.status_code = 406
            response['message'] = "获取openid失败"
            logger.info(u'Failed getting openid.')
            return JsonResponse(response)
        #logger.info(u'Got openid successfully')
        logger.info(u'Got openid successfully with sid {sid}.'.format(sid=account.uid))
        return JsonResponse({'uid': account.uid})


    if request.method == "POST":
        logger.info(u'Got request successfully with method {sid}.'.format(sid=request.body))
        """
        req = json.loads(request.body.decode('utf-8'))
        ed = req.get('ed')  # encrypted_data
        iv = req.get('iv')  # initialization vector
        code = req.get('code')  # code
        """
        code = request.POST['code']  # code
        type = request.POST['type']  # type

        logger.info(u'Received request successfully')
        if (type == 'mp'):
            account = verify_wxmp(code)  # 此步进行数据库的存储或更新
        elif (type == 'web'):
            account = verify_wxweb(code)  # 此步进行数据库的存储或更新

        if not account:
            response = {}
            response.status_code = 406
            response['message'] = "获取openid失败"
            logger.info(u'Failed getting openid.')
            return JsonResponse(response)
        #logger.info(u'Got openid successfully')
        logger.info(u'Got openid successfully with sid {sid}.'.format(sid=account.uid))
        return JsonResponse({'uid': account.uid})
