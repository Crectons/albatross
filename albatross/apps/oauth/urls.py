from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import OpenIDTokenObtainPairView, WechatLoginView

urlpatterns = [
    path('', WechatLoginView.as_view(), name='wechat_login'),  # 微信 mp/web 登录
    path('openid/', OpenIDTokenObtainPairView.as_view(), name='token_obtain_pair'),  # openid登录
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # 刷新token
]
