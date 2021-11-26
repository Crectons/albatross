from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField
from rest_framework_simplejwt.tokens import RefreshToken
import rest_framework_simplejwt.settings

from .auth import OpenIdAuth


class OpenIDTokenObtainPairSerializer(serializers.Serializer):
    """
    OpenID Token 获取序列化器
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['openid'] = PasswordField()  # 前端传入 openid

    @classmethod
    def get_token(cls, user):
        """
        获取 token(access与refresh)

        :param user: user对象

        :return: token 对象
        """
        return RefreshToken.for_user(user)  # 调用 simple-jwt 中 token 生成方法, 需要在 settings 中指定 USER_ID_FIELD 为 uid

    def validate(self, attrs):
        """
        重写验证器

        :param attrs: 序列化器中待验证的数据

        :return: 已验证数据，返回前端
        """

        # 验证 openid
        authenticate_kwargs = {
            'openid': attrs['openid'],  # 给 openid 验证模块准备 openid
        }
        try:
            authenticate_kwargs['request'] = self.context['request']  # 给 openid 验证模块准备请求数据
        except KeyError:
            pass

        openid_auth = OpenIdAuth()  # 实例化 openid 验证模块
        user = openid_auth.authenticate(**authenticate_kwargs)  # 调用 openid 验证模块进行权限验证

        # token 获取
        USER_ID_FIELD = rest_framework_simplejwt.settings.api_settings.USER_ID_FIELD  # 读取 settings 中定义的 user 主键字段名
        data = {}  # 待返回数据
        refresh = self.get_token(user)  # 获取 token
        data[USER_ID_FIELD] = str(getattr(user, USER_ID_FIELD))  # 返回用户id
        data['access'] = str(refresh.access_token)  # 返回 access token
        data['refresh'] = str(refresh)  # 返回 refresh token
        data['is_active'] = user.is_active  # 返回用户激活状态

        return data
