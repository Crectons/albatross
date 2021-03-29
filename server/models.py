from django.db import models

class UserInfo(models.Model):  # 用户信息

    # 微信相关个人信息
    province = models.TextField(default='')
    city = models.TextField(default='')
    session_key = models.TextField(default='')
    avatar = models.TextField(default='')
    openid = models.TextField(default='')

    def __str__(self):
        return self.id_num

    class Meta:
        app_label = 'server'

class Post(models.Model): # 岗位信息

    name = models.TextField(default='') # 岗位名称
    description = models.TextField(default='') # 岗位描述

    def __str__(self):
        return self.id_num

    class Meta:
        app_label = 'server'

#class Enterprises(models.Model): # 企业信息


#class News(models.Model):  # 新闻资讯
