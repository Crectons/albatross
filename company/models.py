from django.db import models

from utils.SoftDelete import SoftDeleteModel


class CompanyInfo(SoftDeleteModel):

    cid = models.AutoField(primary_key=True)

    company_name = models.TextField(default='')  # 公司名称
    company_info = models.TextField(default='')  # 公司信息

    def __str__(self):
        return f'{self.cid}-{self.company_name}'

    class Meta:
        app_label = 'company'
