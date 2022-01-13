from django.urls import path
from rest_framework_extensions.routers import ExtendedSimpleRouter

from . import views

router = ExtendedSimpleRouter()

urlpatterns = [

]

(router.register(r'users', views.UserInfoViewSet, basename='user_info')
 .register(r'intentions', views.UserIntentionViewSet, basename='user_intentions',
           parents_query_lookups=['user_info']
           )
 )

urlpatterns += router.urls
