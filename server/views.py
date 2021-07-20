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
        ban_list_2 = ['产品规划', '产品研发', '电商产品设计']
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
        res = []
        post_list = Post.objects.filter(node_3=category)
        for item in post_list:
            info = {}
            info['pid'] = item.pid
            info['post_name'] = item.post_name
            info['salary'] = item.salary
            info['requirement'] = item.requirement
            info['company_name'] = item.company_name
            info['location'] = item.location
            res.append(info)
        return JsonResponse(res, safe=False)


def getPostInfo(request):
    if request.method == "GET":
        pid = request.GET.get('pid')
        item = Post.objects.filter(pid=pid)
        if not item:
            return HttpResponse(status=404)
        item = item[0]
        res = {}
        res['pid'] = item.pid
        res['node_3'] = item.node_3
        res['post_name'] = item.post_name
        res['salary'] = item.salary
        res['requirement'] = item.requirement
        res['description'] = item.description
        res['welfare'] = item.welfare
        res['company_name'] = item.company_name
        res['company_info'] = item.company_info
        res['location'] = item.location
        return JsonResponse(res)


def getUserInfo(request):
    if request.method == "GET":

        uid = request.GET.get('uid')
        item = UserInfo.objects.filter(uid=uid)
        if not item:
            return HttpResponse(status=404)
        item = item[0]

        res = {}
        res['name'] = item.name
        res['sex'] = item.sex
        res['birth'] = item.birth
        res['location'] = item.location
        res['phone'] = item.phone
        res['email'] = item.email
        res['work_experience'] = item.work_experience
        res['school'] = item.school
        res['qualification'] = item.qualification
        res['major'] = item.major
        res['is_graduate'] = item.is_graduate
        res['edu_details'] = item.edu_details
        res['skills'] = item.skills
        res['training_experience'] = item.training_experience
        res['personal_experience'] = item.personal_experience
        res['self_evaluate'] = item.self_evaluate

        return JsonResponse(res)


def setUserInfo(request):
    if request.method == "GET":

        uid = request.GET.get('uid')
        item = UserInfo.objects.filter(uid=uid)
        if not item:
            return HttpResponse(status=404)
        item = item[0]

        UserInfo.objects.update_or_create(
            uid=uid,
            defaults={
                'name': request.GET.get('name'),
                'sex': request.GET.get('sex'),
                'birth': request.GET.get('birth'),
                'location': request.GET.get('location'),
                'phone': request.GET.get('phone'),
                'email': request.GET.get('email'),
                'work_experience': request.GET.get('work_experience'),
                'school': request.GET.get('school'),
                'qualification': request.GET.get('qualification'),
                'major': request.GET.get('major'),
                'is_graduate': request.GET.get('is_graduate'),
                'edu_details': request.GET.get('edu_details'),
                'skills': request.GET.get('skills'),
                'training_experience': request.GET.get('training_experience'),
                'personal_experience': request.GET.get('personal_experience'),
                'self_evaluate': request.GET.get('self_evaluate'),
            }
        )

        return HttpResponse(status=200)


def addIntention(request):
    if request.method == "GET":
        uid = request.GET.get('uid')
        node_3 = request.GET.get('node_3')
        Intention.objects.create(uid=uid,node_3=node_3)
        return HttpResponse(status=200)


def getAllIntention(request):
    if request.method == "GET":
        uid = request.GET.get('uid')
        result = Intention.objects.filter(uid=uid)
        res = []
        for item in result:
            res.append(item.node_3)
        return JsonResponse(res,safe=False)


def photo(request):  # 图片上传服务
    return HttpResponse(status=200)
