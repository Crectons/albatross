# 重写 jwt 相关验证类
import rest_framework_simplejwt.settings
from django.contrib.auth.backends import BaseBackend
from rest_framework_simplejwt.exceptions import AuthenticationFailed, InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import UserInfo


class OpenIdAuth(BaseBackend):
    """
    OpenID 验证模块(获取token时调用)
    """

    def authenticate(self, request, openid=None, **kwargs):
        """
        重写认证方法

        :param request: 传入请求

        :param openid: 传入openid

        :param kwargs: 字典参数

        :return: openid 对应用户对象
        """
        # 未传入openid 认证失败
        if openid is None:
            return
        # 获取 openid 对应用户
        try:
            user = UserInfo.objects.get(openid=openid)
        except UserInfo.DoesNotExist:
            # openid 无对应用户, 新增用户(is_active 为 false: 未激活)
            user = UserInfo.objects.create(openid=openid)
            print(f"创建用户{user.openid}: {user.uid}")
            user.save()
        return user

    def get_user(self, user_id):
        """
        重写用户获取方法

        :param user_id: uid

        :return: 用户对象
        """
        try:
            user = UserInfo.objects.get(pk=user_id)
        except UserInfo.DoesNotExist:  # 用户不存在, 返回 None
            return None
        return user


class OpenIdJWTAuthentication(JWTAuthentication):
    """
    OpenID JWT 验证模块(访问接口django鉴权时调用)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_model = UserInfo  # 直接限定用户模型，无需修改 django settings 中的默认用户类

    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        api_settings = rest_framework_simplejwt.settings.api_settings  # 获取配置

        # 获取用户 ID
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken('Token contained no recognizable user identification')  # 无用户id, 认证失败

        # 获取用户模型
        try:
            user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed('User not found', code='user_not_found')  # 用户不存在, 认证失败

        if not user.is_active:
            raise AuthenticationFailed('User is inactive', code='user_inactive')  # 用户未激活, 认证失败

        return user
