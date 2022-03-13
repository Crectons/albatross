from django.urls import path
from rest_framework_extensions.routers import ExtendedSimpleRouter, ExtendedDefaultRouter

from . import views


router = ExtendedSimpleRouter()

urlpatterns = [

]

(
    router.register(r'exams', views.ExamViewSet, basename='exam')
    .register('answers', views.ExamQuestionViewSet, basename='examquestion', parents_query_lookups=['id'])
)

urlpatterns += router.urls
