from rest_framework.viewsets import ModelViewSet

from .models import CompanyInfo
from .serializers import CompanyInfoSerializer


class CompanyInfoViewSet(ModelViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
