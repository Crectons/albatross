from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

router.register(r'', views.AreasInfoView, basename='areas')

urlpatterns = [
    url(r'', include(router.urls)),  # 省市区三级信息获取
]

urlpatterns += router.urls
