from django.db import models

from utils.Choice import EducationChoice
from utils.SoftDelete import SoftDeleteModel


class PostTree(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='岗位分类名')
    father = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children', verbose_name='父级分类')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'recruit'
        verbose_name = '岗位树状分类'


class PostInfo(SoftDeleteModel):  # 岗位信息

    pid = models.AutoField(primary_key=True, verbose_name='岗位ID')
    node_1 = models.ForeignKey(PostTree, on_delete=models.CASCADE, null=True, blank=True, verbose_name='一级岗位',
                               related_name='node_1_related')  # 一级岗位
    node_2 = models.ForeignKey(PostTree, on_delete=models.CASCADE, null=True, blank=True, verbose_name='二级岗位',
                               related_name='node_2_related')  # 二级岗位
    node_3 = models.ForeignKey(PostTree, on_delete=models.CASCADE, null=True, blank=True, verbose_name='三级岗位',
                               related_name='node_3_related')  # 三级岗位
    post_name = models.CharField(max_length=100, default='', verbose_name='岗位名称')  # 岗位名称
    salary_low = models.IntegerField(default=0, verbose_name='薪资下限')
    salary_high = models.IntegerField(default=0, verbose_name='薪资上限')
    salary_type = models.BooleanField(null=True, blank=True, verbose_name='薪资类型')  # 薪资类型，0为月薪，1为年薪
    education = models.IntegerField(choices=EducationChoice.choices, default=EducationChoice.ALL, verbose_name='学历要求')  # 岗位学历要求
    experience = models.CharField(max_length=100, default='', verbose_name='工作经验')  # 工作经验
    description = models.TextField(default='', verbose_name='岗位介绍')  # 岗位介绍
    welfare = models.TextField(default='')  # 福利

    company = models.ForeignKey('company.CompanyInfo', on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name='公司')
    location = models.ForeignKey('area.Areas', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='办公地点')

    score = models.IntegerField(default=0, verbose_name='岗位评分')

    def __str__(self):
        return f'{self.pid}: {self.post_name}-{self.company}'

    class Meta:
        app_label = 'recruit'
        verbose_name = '岗位信息'
