import logging

from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins

from .models import UserInfo
from .serializers import UserInfoSerializer, UserIntentionSerializer

logger = logging.getLogger(__name__)


class UserInfoViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):  # 取消 ListModelMixin，阻止列表查询
    """
    用户信息视图
    """
    queryset = UserInfo.objects.all().order_by('uid')  # 按照uid排序
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]  # 仅登录用户可访问个人信息

    def retrieve(self, request, *args, **kwargs):
        """
        重写 retrieve 方法，鉴定用户是否为本人
        """
        if kwargs.get('pk') != str(request.user.uid):
            raise PermissionDenied()  # 权限不足
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserIntentionViewSet(ModelViewSet):  # TODO: 求职意向返回待完善
    """
    用户意向视图
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserIntentionSerializer
    permission_classes = [IsAuthenticated]
