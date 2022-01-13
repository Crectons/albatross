from django_filters.rest_framework import FilterSet
import django_filters

from .models import PostTree, PostInfo


class PostTreeFilter(FilterSet):
    """
    岗位分类过滤器
    """
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')  # icontains，包含且忽略大小写
    id = django_filters.NumberFilter(field_name='id', lookup_expr='exact')  # exact，精确匹配
    type = django_filters.NumberFilter(field_name='type', lookup_expr='exact')  # exact，精确匹配

    class Meta:
        # 指定模型
        models = PostTree
        # 指定查询的字段
        fields = ['name', 'id', 'type']


class PostInfoFilter(FilterSet):
    """
    岗位分类过滤器
    """
    name = django_filters.CharFilter(field_name='post_name', lookup_expr='icontains')  # icontains，包含且忽略大小写
    pid = django_filters.NumberFilter(field_name='pid', lookup_expr='exact')  # exact，精确匹配

    node_1 = django_filters.NumberFilter(field_name='node_1', lookup_expr='exact')
    node_2 = django_filters.NumberFilter(field_name='node_2', lookup_expr='exact')
    node_3 = django_filters.NumberFilter(field_name='node_3', lookup_expr='exact')

    salary_min = django_filters.NumberFilter(field_name='salary_max', lookup_expr='gte')
    salary_max = django_filters.NumberFilter(field_name='salary_min', lookup_expr='lt')

    location = django_filters.NumberFilter(field_name='location', lookup_expr='exact')
    location_min = django_filters.NumberFilter(field_name='location', lookup_expr='gte')
    location_max = django_filters.NumberFilter(field_name='location', lookup_expr='lt')

    requirement = django_filters.NumberFilter(field_name='requirement', lookup_expr='exact')
    requirement_min = django_filters.NumberFilter(field_name='requirement', lookup_expr='gte')
    requirement_max = django_filters.NumberFilter(field_name='requirement', lookup_expr='lt')

    priority = django_filters.BooleanFilter(field_name='priority')

    class Meta:
        # 指定模型
        models = PostInfo
        # 指定查询的字段
        fields = ['name', 'pid', 'node_1', 'node_2', 'node_3', 'salary_min', 'salary_max',
                  'location', 'location_min', 'location_max', 'requirement', 'requirement_min', 'requirement_max',
                  'priority']
