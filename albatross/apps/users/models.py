from django.db import models

from albatross.utils.SoftDelete import SoftDeleteModel
from albatross.utils.choices import GenderChoice
from albatross.utils.choices import EducationChoice


class UserInfo(SoftDeleteModel):
    """
    用户信息
    """

    uid = models.AutoField(primary_key=True, verbose_name='用户ID')

    # 微信相关个人信息
    province = models.TextField(default='', verbose_name='省份')
    city = models.TextField(default='', verbose_name='城市')
    session_key = models.TextField(default='')
    avatar = models.ImageField(upload_to='avatar', default='', verbose_name='头像')
    openid = models.TextField(default='')

    # 个人基本信息
    name = models.CharField(max_length=16, default='', verbose_name='姓名')  # 姓名
    sex = models.SmallIntegerField(choices=GenderChoice.choices, default=GenderChoice.SECRET,
                                   verbose_name='性别')  # 性别
    birth = models.DateField(null=True, blank=True, verbose_name='生日')  # 生日
    location = models.CharField(max_length=200, default='', verbose_name='居住地')  # 居住地
    phone = models.CharField(max_length=11, default='', verbose_name='电话')  # 电话
    email = models.CharField(max_length=100, default='', verbose_name='邮箱')  # 邮箱

    work_experience = models.TextField(default='', verbose_name='工作经历')  # 工作经历
    school = models.TextField(default='', verbose_name='学校')  # 学校
    qualification = models.IntegerField(choices=EducationChoice.choices, default=EducationChoice.UNKNOWN,
                                        verbose_name='学历')
    major = models.CharField(max_length=100, default='', verbose_name='专业')  # 专业
    is_graduate = models.BooleanField(default=False, verbose_name='应届生')  # 是否为应届生
    edu_details = models.TextField(default='', verbose_name='教育经历详情')  # 教育经历详情

    skills = models.TextField(default='', verbose_name='技能')  # 技能
    training_experience = models.TextField(default='', verbose_name='培训经历')  # 培训经历
    personal_experience = models.TextField(default='', verbose_name='个人经历')  # 个人经历
    self_evaluate = models.TextField(default='', verbose_name='自我评价')  # 自我评价

    intention = models.ManyToManyField('recruits.PostTree', verbose_name='求职意向', default=None, blank=True)

    def __str__(self):
        return f'{self.uid}: {self.name}'

    class Meta:
        app_label = 'users'
        db_table = 'tb_user_info'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

