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
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from user import views as user_views
from recruit import views as recruit_views
from company import views as company_views

urlpatterns = [
    url(r'docs/', include_docs_urls(title='接口文档')),
    path(r'area/', include('area.urls')),
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'user', user_views.UserInfoViewSet)
router.register(r'post', recruit_views.PostInfoViewSet)
router.register(r'classification', recruit_views.PostTreeViewSet)
router.register(r'company', company_views.CompanyInfoViewSet)

urlpatterns += router.urls
