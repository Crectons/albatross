from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.response import Response
from rest_framework import status

from .serializers import OpenIDTokenObtainPairSerializer
from users.models import UserInfo


class MyTokenObtainPairView(TokenObtainPairView):
    queryset = UserInfo.objects.all()
    serializer_class = OpenIDTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
