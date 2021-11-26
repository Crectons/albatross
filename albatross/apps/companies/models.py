from django.db import models

from albatross.utils.SoftDelete import SoftDeleteModel


class CompanyInfo(SoftDeleteModel):

    cid = models.AutoField(primary_key=True)

    company_name = models.TextField(default='')  # 公司名称
    company_info = models.TextField(default='')  # 公司信息

    def __str__(self):
        return f'{self.cid}-{self.company_name}'

    class Meta:
        app_label = 'companies'
        db_table = 'tb_company_info'
        verbose_name = '公司'
        verbose_name_plural = verbose_name
