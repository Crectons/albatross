from django.shortcuts import render
import hashlib
import json

from django.http import HttpResponse, JsonResponse
# from django.core import serializers
from oauth.utils import verify_request
from weixin.lib.wxcrypt import WXBizDataCrypt

from server.tasks import *
from server.models import *


def test(request):
    return HttpResponse(status=200)


def userInfoRelated(request):
    if request.method == "GET":
        uid = request.GET.get('uid')
        user = UserInfo.objects.get(uid=uid)
        res = {
            'name': user.name,
            'sex': user.sex,
            'age': user.age,
            'phone': user.phone,
            'email': user.email,
            'educational_experience': user.educational_experience,
            'opration_experience': user.opration_experience,
            'language_ability': user.language_ability,
            'personal_works': user.personal_works,

        }
        return JsonResponse(res)

    if request.method == "POST":
        req = json.loads(request.body.decode())
        UserInfo.objects.get(uid=req.get('uid')).update(
            name=req.get('name'),
            sex=req.get('sex'),
            age=req.get('age'),
            phone=req.get('phone'),
            email=req.get('email'),
            educational_experience=req.get('educational_experience'),
            opration_experience=req.get('opration_experience'),
            language_ability=req.get('language_ability'),
            personal_works=req.get('personal_works'),
        )
        return HttpResponse(status=200)



def getPostTree(request):
    if request.method == "GET":
        res = {}
        ban_list_2 = ['产品规划','产品研发','电商产品设计']
        ban_list_3 = ['产品']
        info = PostTree.objects.all()
        for item in info:
            if item.name_father == '根':
                res[item.name_son] = {}
                for sub_item in info:
                    if sub_item.name_father == item.name_son:
                        if sub_item.name_son in ban_list_2:
                            continue
                        if not res[item.name_son].__contains__(sub_item.name_son):
                            res[item.name_son][sub_item.name_son] = []
                        for sub_sub_item in info:
                            if sub_sub_item.name_father == sub_item.name_son:
                                if sub_sub_item.name_son in ban_list_3:
                                    continue
                                if sub_sub_item.name_son not in res[item.name_son][sub_item.name_son]:
                                    res[item.name_son][sub_item.name_son].append(sub_sub_item.name_son)
        return JsonResponse(res)


def getAllPost(request):
    if request.method == "GET":
        category = request.GET.get('category')
        res = {}
        res['post_list'] = []
        post_list = Post.objects.filter(node_3=category)
        for item in post_list:
            info = {}
            info['post_name'] = item.post_name
            info['salary'] = item.salary
            info['requirement'] = item.requirement
            info['company_name'] = item.company_name
            info['location'] = item.location
            res['post_list'].append(info)
        return JsonResponse(res)


def getPostInfo(request):
    if request.method == "GET":
        return True


def photo(request):  # 图片上传服务
    return HttpResponse(status=200)
