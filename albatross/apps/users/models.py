from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


from albatross.utils.models import SoftDeleteModel
from albatross.utils.choices import GenderChoice
from albatross.utils.choices import EducationChoice
from albatross.utils.storage import AvatarStorage
from areas.models import Areas


class UserInfo(SoftDeleteModel, AbstractBaseUser):
    """
    用户信息 继承于 AbstractBaseUser 便于 jwt 鉴权
    """

    uid = models.AutoField(primary_key=True, verbose_name='用户ID')
    password = None  # 无需 password 字段

    # 微信相关个人信息 TODO: 待完善具体信息
    province = models.ForeignKey(to=Areas, on_delete=models.CASCADE, verbose_name='省份', blank=True, null=True,
                                 related_name='province')
    city = models.ForeignKey(to=Areas, on_delete=models.CASCADE, verbose_name='城市', blank=True, null=True,
                             related_name='city')
    avatar = models.ImageField(upload_to='avatar', default='avatar/default.jpg', verbose_name='头像',
                               storage=AvatarStorage)
    openid = models.CharField(max_length=50, default='')

    # 个人基本信息
    name = models.CharField(max_length=16, default='', verbose_name='姓名')  # 姓名
    birth = models.DateField(null=True, blank=True, verbose_name='生日')  # 生日
    sex = models.SmallIntegerField(choices=GenderChoice.choices, default=GenderChoice.SECRET,
                                   verbose_name='性别')  # 性别
    location = models.ForeignKey(to=Areas, on_delete=models.CASCADE, verbose_name='居住地', blank=True, null=True,
                                 related_name='location')  # 居住地
    phone = models.CharField(max_length=11, default='', verbose_name='电话')  # 电话
    email = models.CharField(max_length=100, default='', verbose_name='邮箱')  # 邮箱

    # 教育经历
    school = models.TextField(default='', verbose_name='学校')  # 学校
    major = models.CharField(max_length=100, default='', verbose_name='专业')  # 专业
    qualification = models.IntegerField(choices=EducationChoice.choices, default=EducationChoice.UNKNOWN,
                                        verbose_name='学历')
    is_graduate = models.BooleanField(default=False, verbose_name='应届生')  # 是否为应届生
    edu_details = models.TextField(default='', verbose_name='教育经历详情')  # 教育经历详情

    work_experience = models.TextField(default='', verbose_name='工作经历')  # 工作经历
    skills = models.TextField(default='', verbose_name='技能')  # 技能
    training_experience = models.TextField(default='', verbose_name='培训经历')  # 培训经历
    personal_experience = models.TextField(default='', verbose_name='个人经历')  # 个人经历
    self_evaluate = models.TextField(default='', verbose_name='自我评价')  # 自我评价

    is_active = models.BooleanField(default=False, verbose_name='是否激活')  # 是否激活

    def __str__(self):
        return f'{self.uid}: {self.name}'

    class Meta:
        app_label = 'users'
        db_table = 'tb_user_info'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class UserIntention(models.Model):
    """
    用户意向
    """
    user = models.ForeignKey(to=UserInfo, related_name='intention', on_delete=models.CASCADE, verbose_name='用户')
    post = models.ForeignKey(to='recruits.PostTree', on_delete=models.CASCADE, verbose_name='岗位分类')
    salary = models.IntegerField(default=0, verbose_name='薪资')
    city = models.ForeignKey(to=Areas, on_delete=models.CASCADE, null=True, blank=True, verbose_name='城市')
    language = models.CharField(max_length=100, default='', verbose_name='语言')
    platform = models.CharField(max_length=100, default='', verbose_name='平台')
    working_type = models.CharField(max_length=100, default='', verbose_name='工作类型')
    area = models.CharField(max_length=100, default='', verbose_name='地区')

    class Meta:
        app_label = 'users'
        db_table = 'tb_user_intention'
        verbose_name = '用户意向'
        verbose_name_plural = verbose_name
