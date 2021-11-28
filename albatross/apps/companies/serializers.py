from rest_framework.serializers import ModelSerializer

from .models import CompanyInfo


class CompanyInfoSerializer(ModelSerializer):
    """
    公司信息序列化器
    """
    class Meta:
        model = CompanyInfo
        exclude = ['is_deleted', 'info', 'create_time', 'update_time']  # 不返回 is_deleted 字段


class CompanyInfoDetailSerializer(ModelSerializer):
    """
    公司信息序列化器
    """
    class Meta:
        model = CompanyInfo
        exclude = ['is_deleted']
