from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import UserInfo


class UserInfoSerializer(ModelSerializer):
    """
    用户信息序列化器（所有信息）
    """
    class Meta:
        model = UserInfo
        exclude = ['is_deleted']

    # # intention 返回 str
    # intention = SerializerMethodField()
    #
    # def get_intention(self, obj):
    #     tags_list = []
    #     tags = obj.intention.all()
    #     for tag in tags:
    #         tags_list.append(tag.name)
    #     return tags_list


class UserIntentionSerializer(ModelSerializer):
    """
    用户求职意向序列化器
    """

    class Meta:
        model = UserInfo
        fields = ['uid', 'intention']
