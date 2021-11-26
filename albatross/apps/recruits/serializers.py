from rest_framework.serializers import ModelSerializer

from .models import PostTree, PostInfo


class PostTreeSerializer(ModelSerializer):
    """
    岗位分类序列化器
    """
    class Meta:
        model = PostTree
        fields = '__all__'


class PostInfoSerializer(ModelSerializer):
    """
    岗位信息序列化器
    """
    class Meta:
        model = PostInfo
        exclude = ['is_deleted']
