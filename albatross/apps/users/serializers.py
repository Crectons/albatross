from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import UserInfo


class UserInfoSerializer(ModelSerializer):
    """
    用户信息序列化器（所有信息）
    """
    class Meta:
        model = UserInfo
        exclude = ['is_deleted']

    # 目前无需返回岗位分类字符串，建议前端预先存储posttree的dict字典便于后续操作
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
