from rest_framework import serializers
from rest_framework.exceptions import NotAuthenticated
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework_extensions.mixins import NestedViewSetMixin

from areas.models import Areas
from recruits.serializers import PostTreeSerializer
from .models import UserInfo, UserIntention


class UserInfoSerializer(NestedViewSetMixin, ModelSerializer):
    """
    用户信息序列化器（所有信息）
    """
    class Meta:
        model = UserInfo
        exclude = ['is_deleted', 'last_login', 'openid']

    def validate_avatar(self, value):
        """
        头像检测
        """
        if not value:  # 未找到头像文件
            return 'media/avatar/default.jpg'

        if value.content_type not in ['image/jpeg', 'image/png', 'image/gif']:  # 文件类型不正确
            raise serializers.ValidationError(detail='Avatar is not a image', code='avatar_not_image')

        if value.size > 1024 * 1024 * 2:  # 头像文件大于2M
            raise serializers.ValidationError(detail='Avatar is larger than 2MB', code='avatar_too_large')
        if value.size < 1024:  # 头像文件小于1KB
            raise serializers.ValidationError(detail='Avatar is smaller than 1KB', code='avatar_too_small')

        if self.instance.avatar != 'media/avatar/default.jpg':  # 已存在头像文件
            self.instance.avatar.delete()  # 删除原头像文件

        return value


class UserIntentionSerializer(NestedViewSetMixin, ModelSerializer):
    """
    用户求职意向序列化器
    """
    city_str = serializers.CharField(source='city', label='城市')
    post_str = serializers.StringRelatedField(source='post', label='岗位', read_only=True)

    def validate_city_str(self, value):
        """
        城市字符串转换
        """
        if value:
            try:
                city = Areas.objects.get(name=value.split('-')[-1])
            except Areas.DoesNotExist:
                raise serializers.ValidationError(detail='城市不存在', code='city_not_exist')
            return city
        return None

    def validate(self, attrs):
        """
        添加 user
        """
        # 添加 user
        if self.context['request'].user.is_anonymous:
            raise NotAuthenticated('用户未登录')
        attrs['user'] = self.context['request'].user
        return attrs

    class Meta:
        model = UserIntention
        exclude = ['user']
