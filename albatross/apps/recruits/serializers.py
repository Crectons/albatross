from rest_framework.serializers import ModelSerializer

from .models import PostTree, PostInfo


class PostTreeSerializer(ModelSerializer):
    class Meta:
        model = PostTree
        fields = '__all__'


class PostInfoSerializer(ModelSerializer):
    class Meta:
        model = PostInfo
        exclude = ['is_deleted']
