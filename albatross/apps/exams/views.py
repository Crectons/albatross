from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import UserInfo
from . import models
from . import serializers
from . import tasks


class ExamViewSet(viewsets.ModelViewSet):
    """
    试卷视图集
    """
    queryset = models.Exam.objects.order_by('-update_time')
    serializer_class = serializers.ExamSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ExamListSerializer
        elif self.action in ['submit_detail', 'submit']:
            return serializers.ExamResultSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        single_num = int(request.data.get('single_num', 0))
        multiple_num = int(request.data.get('multiple_num', 0))
        judge_num = int(request.data.get('judge_num', 0))
        user = UserInfo.objects.get(uid=1)
        exam_name = request.data.get('exam_name')

        # 创建试卷
        exam = tasks.create_random_exam(exam_name, user, single_num, multiple_num, judge_num)

        serializer = self.get_serializer(exam)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['post'], detail=True)
    def submit(self, request, pk=None):
        instance = self.get_object()
        tasks.revise_exam(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def submit_detail(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ExamQuestionViewSet(viewsets.ModelViewSet):
    """
    试卷题目视图集
    """
    queryset = models.ExamQuestion
    serializer_class = serializers.AnswerSerializer
    pagination_class = None

    def get_queryset(self):
        exam_id = self.kwargs['parent_lookup_id']
        return models.ExamQuestion.objects.filter(exam_id=exam_id)

    def update_answer(self, request, partial, *args, **kwargs):
        for answer in request.data:
            instance = models.ExamQuestion.objects.get(id=answer['id'])
            serializer = self.get_serializer(instance, data=answer, partial=partial)
            serializer.is_valid(raise_exception=True)
            serializer.save()

    def put(self, request, *args, **kwargs):
        self.update_answer(request, partial=True, *args, **kwargs)
        return self.list(self, request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
