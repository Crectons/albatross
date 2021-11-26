from rest_framework.serializers import ModelSerializer

from .models import CompanyInfo


class CompanyInfoSerializer(ModelSerializer):
    """
    公司信息序列化器
    """
    class Meta:
        model = CompanyInfo
        exclude = ['is_deleted']
