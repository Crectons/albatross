from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.response import Response
from rest_framework import status

from .serializers import OpenIDTokenObtainPairSerializer, WechatLoginSerializer
from users.models import UserInfo


class OpenIDTokenObtainPairView(TokenObtainPairView):
    """
    open id 登录视图
    """
    queryset = UserInfo.objects.all()
    serializer_class = OpenIDTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        """
        重写 post 方法, 增加 open id 登录
        """
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class WechatLoginView(OpenIDTokenObtainPairView):
    """
    微信登录视图
    """
    queryset = UserInfo.objects.all()
    serializer_class = WechatLoginSerializer
