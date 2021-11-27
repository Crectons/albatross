from rest_framework.serializers import ModelSerializer

from .models import PostTree, PostInfo


class PostTreeSerializer(ModelSerializer):
    """
    岗位分类序列化器
    """
    class Meta:
        model = PostTree
        exclude = ['father']


class PostTreeDetailSerializer(ModelSerializer):
    """
    岗位分类嵌套序列化器
    """
    children = PostTreeSerializer(many=True, read_only=True)

    class Meta:
        model = PostTree
        exclude = ['father']


class PostInfoSerializer(ModelSerializer):
    """
    岗位信息序列化器
    """
    class Meta:
        model = PostInfo
        exclude = ['is_deleted']
