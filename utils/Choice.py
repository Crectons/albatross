from django.db import models


class GenderChoice(models.IntegerChoices):
    SECRET = 0, 'Secret'
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'


class EducationChoice(models.IntegerChoices):
    UNKNOWN = 0, '未知'
    ALL = 1, '不限'
    XIAO_XUE = 2, '小学'
    CHU_ZHONG = 3, '初中'
    GAO_ZHONG = 4, '高中'
    ZHONG_ZHUAN = 5, '中专'
    DA_ZHAUN = 6, '大专'
    BEN_KE = 7, '本科'
    SHUO_SHI = 8, '硕士'
    BO_SHI = 9, '博士'
