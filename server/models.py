from django.db import models

class UserInfo(models.Model):  # 用户信息

    uid = models.AutoField(primary_key=True)

    # 微信相关个人信息
    province = models.TextField(default='')
    city = models.TextField(default='')
    session_key = models.TextField(default='')
    avatar = models.TextField(default='')
    openid = models.TextField(default='')

    # 个人基本信息
    name = models.TextField(default='')  # 姓名
    sex = models.IntegerField(default='')  # 性别 男0女1
    age = models.IntegerField(default='')  # 年龄
    phone = models.TextField(default='')  # 电话
    email = models.TextField(default='')  # 邮箱

    educational_experience = models.TextField(default='')  # 教育经历
    opration_experience = models.TextField(default='')  # 跨境平台运营经历
    language_ability = models.TextField(default='')  # 外语能力
    personal_works = models.TextField(default='')  # 个人作品

    def __str__(self):
        return self.id_num

    class Meta:
        app_label = 'server'

class Post(models.Model): # 岗位信息

    #pid = models.AutoField(primary_key=True)
    cid = models.IntegerField(default='')
    node_1 = models.TextField(default='')  # 一级岗位
    node_2 = models.TextField(default='')  # 二级岗位
    node_3 = models.TextField(default='')  # 三级岗位
    post_name = models.TextField(default='')  # 岗位名称
    salary = models.TextField(default='')  # 岗位名称
    #salary_low = models.TextField(default='')  # 薪水下限
    #salary_high = models.TextField(default='')  # 薪水上限
    requirement = models.TextField(default='')  # 岗位要求
    description = models.TextField(default='')  # 岗位介绍
    welfare = models.TextField(default='')  # 福利
    company_name = models.TextField(default='')  # 公司名称
    company_info = models.TextField(default='')  # 公司信息
    location = models.TextField(default='')  # 办公地点


    def __str__(self):
        return self.id_num

    class Meta:
        app_label = 'server'

class PostTree(models.Model): # 岗位信息

    name_father = models.TextField(default='')  # 父节点名称
    name_son = models.TextField(default='')  # 子节点名称

    def __str__(self):
        return self.id_num

    class Meta:
        app_label = 'server'

class company(models.Model):

    cid = models.AutoField(primary_key=True)

    def __str__(self):
        return self.id_num

    class Meta:
        app_label = 'server'

#class News(models.Model):  # 新闻资讯
