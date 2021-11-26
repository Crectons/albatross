from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import CompanyInfo
from .serializers import CompanyInfoSerializer


class CompanyInfoViewSet(ModelViewSet):
    """
    公司信息视图
    """
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [AllowAny]  # 任何人可访问 TODO:修改权限待设定
