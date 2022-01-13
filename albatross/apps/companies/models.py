from django.db import models

from albatross.utils.models import SoftDeleteModel


class CompanyInfo(SoftDeleteModel):
    """
    公司信息
    """

    cid = models.AutoField(primary_key=True)  # 公司 ID

    name = models.CharField(max_length=100, unique=True, verbose_name='公司名称')  # 公司名称
    info = models.TextField(default='', verbose_name='公司详细信息')  # 公司详细信息

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'companies'
        db_table = 'tb_company_info'
        verbose_name = '公司'
        verbose_name_plural = verbose_name
