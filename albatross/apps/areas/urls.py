from django.conf.urls import url, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'info', AreasInfoView, basename='info')

urlpatterns = [
    url(r'', include(router.urls)),  # 省市区三级信息获取
]

