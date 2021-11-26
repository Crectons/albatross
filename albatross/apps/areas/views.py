from rest_framework.permissions import AllowAny
from rest_framework.viewsets import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import *
from .models import *


class AreasInfoView(ReadOnlyModelViewSet, CacheResponseMixin):
    permission_classes = [AllowAny]
    """提供省市区三级联动数据"""

    # 禁用分页
    pagination_class = None

    # 指定要输出的数据来自哪个查询集
    # queryset = Area.objects.all()
    def get_queryset(self):
        """根据请求的行为，过滤不同的行为对应的序列化器需要的数据"""
        if self.action == 'list':
            return Areas.objects.filter(pid=None)  # 只有当pid=None 返回的是省级数据
        else:
            return Areas.objects.all()

    # 指定序列化器
    # serializer_class = ‘序列化器‘
    def get_serializer_class(self):
        """根据请求的行为，指定不同的序列化器"""
        if self.action == 'list':
            return AreaInfoSer
        else:
            return NextAreasInfoSer
