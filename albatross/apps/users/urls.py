from django.urls import path
from rest_framework_extensions.routers import ExtendedSimpleRouter

from . import views

router = ExtendedSimpleRouter()

urlpatterns = [

]

(router.register(r'users', views.UserInfoViewSet, basename='user')
 .register(r'intentions', views.UserIntentionViewSet, basename='user_intentions',
           parents_query_lookups=['user']
           )
 )

(router.register(r'users', views.UserInfoViewSet, basename='user')
 .register(r'resumes', views.UserPostResumeViewSet, basename='user_resumes',
           parents_query_lookups=['user']
           )
 )

urlpatterns += router.urls
