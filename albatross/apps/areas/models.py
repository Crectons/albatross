from django.db import models


class Areas(models.Model):
    """
    省市区数据
    """
    name = models.CharField(max_length=50, verbose_name='地名')
    pid = models.ForeignKey('self', verbose_name='父级的行政区域id', on_delete=models.SET_NULL, related_name='addinfo',
                            null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'areas'
        db_table = 'tb_areas'
        verbose_name = '地区'
