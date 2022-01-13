from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import PostTree, PostInfo, PostResume
from companies.serializers import CompanyInfoDetailSerializer


class PostTreeSerializer(ModelSerializer):
    """
    岗位分类序列化器
    """
    class Meta:
        model = PostTree
        fields = '__all__'
        extra_kwargs = {
            'father': {'write_only': True},
        }


class PostTreeDetailSerializer(ModelSerializer):
    """
    岗位分类嵌套序列化器
    """
    children = PostTreeSerializer(many=True, read_only=True)

    class Meta:
        model = PostTree
        fields = '__all__'
        extra_kwargs = {
            'father': {'write_only': True},
        }


class PostInfoListSerializer(ModelSerializer):
    """
    岗位信息序列化器
    """
    class Meta:
        model = PostInfo
        fields = ['pid', 'update_time', 'post_name', 'salary_min', 'company', 'requirement',
                  'node_1', 'node_2', 'node_3', 'location', 'recommend', 'priority']

    company = serializers.StringRelatedField(label='公司名称', read_only=True)
    node_1 = serializers.StringRelatedField(label='一级分类', read_only=True)
    node_2 = serializers.StringRelatedField(label='二级分类', read_only=True)
    node_3 = serializers.StringRelatedField(label='三级分类', read_only=True)

    location = serializers.StringRelatedField(label='地区', read_only=True)


class PostInfoDetailSerializer(PostInfoListSerializer):
    class Meta:
        model = PostInfo
        exclude = ['is_deleted']

    company = CompanyInfoDetailSerializer(label='公司名称', read_only=True)


class PostInfoCreateSerializer(ModelSerializer):
    class Meta:
        model = PostInfo
        exclude = ['is_deleted']


class PostResumeSerializer(ModelSerializer):
    class Meta:
        model = PostResume
        fields = '__all__'
