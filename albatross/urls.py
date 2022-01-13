from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from django.views.static import serve
from django.conf import settings

from users import views as user_views
from recruits import views as recruit_views
from companies import views as company_views

urlpatterns = [
    path('admin/', admin.site.urls),  # admin 后台管理
    path(r'areas/', include('areas.urls')),  # 省市区获取接口
    path('token/', include('oauth.urls')),  # openid 登录
    path('users/', include('users.urls')),  # 用户信息
    path('recruits/', include('recruits.urls')),  # 招聘信息
    path('companies/', include('companies.urls')),  # 公司信息
    url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]

router = routers.DefaultRouter()

urlpatterns += router.urls
