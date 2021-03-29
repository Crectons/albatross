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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from server import views as server_views
from oauth import views as oauth_views
from apiblueprint_view.views import ApiBlueprintView

urlpatterns = [
    url(r'^docs/$', ApiBlueprintView.as_view(blueprint=r'~/albatross/apiary.apib')),
    path('', csrf_exempt(server_views.test)),
    path('test/', csrf_exempt(server_views.test)),
    path('admin/', admin.site.urls),
    path('photo/', csrf_exempt(server_views.photo)),
    path('login/',csrf_exempt(oauth_views.oauth)),
]
