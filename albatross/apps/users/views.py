import logging

from rest_framework.exceptions import PermissionDenied
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
                      GenericViewSet):
    queryset = UserInfo.objects.all().order_by('uid')
    serializer_class = UserInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') != str(request.user.uid):
            raise PermissionDenied()
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserIntentionViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserIntentionSerializer
