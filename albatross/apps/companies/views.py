from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import CompanyInfo
from .serializers import CompanyInfoSerializer


class CompanyInfoViewSet(ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [AllowAny]
