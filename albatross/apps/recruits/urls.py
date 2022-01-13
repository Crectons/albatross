from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()

urlpatterns = [
    
]

router.register(r'post', views.PostInfoViewSet)  # post info
router.register(r'post_tree', views.PostTreeViewSet, basename='post_tree')  # 岗位分类

urlpatterns += router.urls
