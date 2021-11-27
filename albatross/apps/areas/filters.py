from django_filters.rest_framework import FilterSet
import django_filters

from .models import Areas


class AreaFilter(FilterSet):
    """
    地区过滤器
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')  # exact，精确匹配

    class Meta:
        # 指定模型
        models = Areas
        # 指定查询的字段
        fields = ['name', 'id']
