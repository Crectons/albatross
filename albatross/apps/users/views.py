import logging
from rest_framework.viewsets import ModelViewSet


from .models import UserInfo
from .serializers import UserInfoSerializer, UserIntentionSerializer

logger = logging.getLogger(__name__)


class UserInfoViewSet(ModelViewSet):
    queryset = UserInfo.objects.all().order_by('uid')
    serializer_class = UserInfoSerializer
    exclude = ['is_deleted']


class UserIntentionViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserIntentionSerializer
