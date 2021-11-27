"""albatross URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from users import views as user_views
from recruits import views as recruit_views
from companies import views as company_views

urlpatterns = [
    path(r'area/', include('areas.urls')),  # 省市区获取接口
    path('admin/', admin.site.urls),  # admin 后台管理
    path('token/', include('oauth.urls')),  # openid 登录
]

router = routers.DefaultRouter()
router.register(r'user', user_views.UserInfoViewSet)  # 用户信息
router.register(r'post', recruit_views.PostInfoViewSet)  # 招聘信息
router.register(r'posttree', recruit_views.PostTreeViewSet, basename='posttree')  # 岗位分类(视图中未直接指定查询集，此处需要指定basename)
router.register(r'company', company_views.CompanyInfoViewSet)  # 公司信息

urlpatterns += router.urls
