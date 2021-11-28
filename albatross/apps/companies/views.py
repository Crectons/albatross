from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .filters import CompanyInfoFilter
from .models import CompanyInfo
from .serializers import CompanyInfoSerializer, CompanyInfoDetailSerializer


class CompanyInfoViewSet(ModelViewSet):
    """
    公司信息视图
    """
    queryset = CompanyInfo.objects.order_by('cid')
    permission_classes = [AllowAny]  # 任何人可访问 TODO:修改权限待设定
    filterset_class = CompanyInfoFilter

    def get_serializer_class(self):
        """
        获取序列化器类
        """
        if self.action == 'list':
            return CompanyInfoSerializer
        return CompanyInfoDetailSerializer
