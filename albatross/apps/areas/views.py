from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import *
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .filters import AreaFilter
from .serializers import *
from .models import *


class AreasInfoView(ReadOnlyModelViewSet, CacheResponseMixin):
    """
    提供省市区三级联动数据
    """
    filterst_class = AreaFilter  # 过滤器
    permission_classes = [AllowAny]  # 任何人可访问
    pagination_class = None  # 禁用分页

    # 指定要输出的数据来自哪个查询集
    # queryset = Area.objects.all()
    def get_queryset(self):
        """
        根据请求的行为，过滤不同的行为对应的序列化器需要的数据
        """
        if self.action == 'list':
            return Areas.objects.filter(pid=None)  # 只有当 pid=None 返回的是省级数据
        else:
            return Areas.objects.all()

    # 指定序列化器
    # serializer_class = 序列化器
    def get_serializer_class(self):
        """
        根据请求的行为，指定不同的序列化器
        """
        if self.action == 'list':
            return AreaInfoSer
        else:
            return NextAreasInfoSer

    @action(methods=['get'], detail=False)
    def all(self, request):
        queryset = self.filter_queryset(Areas.objects.all())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = AreaInfoSer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AreaInfoSer(queryset, many=True)
        return Response(serializer.data)
