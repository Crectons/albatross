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
    sex = models.TextField(default='')  # 性别
    birth = models.TextField(default='')  # 生日
    # age = models.IntegerField(default='')  # 年龄
    location = models.TextField(default='')  # 居住地
    phone = models.TextField(default='')  # 电话
    email = models.TextField(default='')  # 邮箱

    work_experience = models.TextField(default='')  # 工作经历
    school = models.TextField(default='')  # 学校
    qualification = models.TextField(default='')  # 学历
    major = models.TextField(default='')  # 专业
    is_graduate = models.TextField(default='')  # 应届生/毕业生
    edu_details = models.TextField(default='')  # 教育经历详情

    skills = models.TextField(default='')  # 技能
    training_experience = models.TextField(default='')  # 培训经理
    personal_experience = models.TextField(default='')  # 个人经历
    self_evaluate = models.TextField(default='')  # 自我评价

    def __str__(self):
        return self.id_num

    class Meta:
        app_label = 'server'

class Post(models.Model): # 岗位信息

    pid = models.AutoField(primary_key=True)
    #cid = models.IntegerField(default='')
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
