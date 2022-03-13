from rest_framework import serializers

from . import models


class QuestionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionChoice
        fields = ['id', 'content']


class QuestionSerializer(serializers.ModelSerializer):
    choice = QuestionChoiceSerializer(source='questionchoice_set', many=True)

    class Meta:
        model = models.Question
        fields = ['id', 'type', 'content', 'choice']


class ExamQuestionSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = models.ExamQuestion
        fields = ['id', 'question', 'answer', 'full_score']
        read_only_fields = ['id', 'question', 'full_score']


class ExamQuestionResultSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()
    correct_answer = serializers.SerializerMethodField()

    def get_correct_answer(self, obj):
        result = []
        for choice in obj.question.questionchoice_set.filter(is_correct=True):
            result.append(choice.id)
        return result

    class Meta:
        model = models.ExamQuestion
        fields = ['id', 'question', 'answer', 'correct_answer', 'score', 'full_score']


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExamQuestion
        fields = ['id', 'answer']


class ExamSerializer(serializers.ModelSerializer):
    content = ExamQuestionSerializer(source='examquestion_set', many=True)

    class Meta:
        model = models.Exam
        fields = ['id', 'name', 'content', 'submit', 'score', 'total_score', 'create_time', 'update_time']


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exam
        fields = ['id', 'name', 'submit', 'score', 'total_score', 'create_time', 'update_time']


class ExamResultSerializer(serializers.ModelSerializer):
    content = ExamQuestionResultSerializer(source='examquestion_set', many=True)

    class Meta:
        model = models.Exam
        fields = ['id', 'name', 'content', 'submit', 'score', 'total_score', 'create_time', 'update_time']
