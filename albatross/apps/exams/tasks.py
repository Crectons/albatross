from typing import List

from django.db.models import Sum
from rest_framework.exceptions import ValidationError

from albatross.utils.choices import QuestionTypeChoice
from users.models import UserInfo
from . import models


def get_random_question(question_type: QuestionTypeChoice, num: int):
    """
    随机获取试题
    :param question_type: 种类
    :param num: 数量
    :return: question 列表
    """
    if num < 0 or num > models.Question.objects.filter(type=question_type).count():
        raise ValidationError('num must be in [0, %d]' % models.Question.objects.filter(type=type).count())
    return models.Question.objects.filter(type=question_type).order_by('?')[:num]


def create_exam_question_by_type(exam: models.Exam, question: List[models.Question], score: int):
    """
    创建测试题目
    :param exam: 考试
    :param question: 题目列表
    :param score: 分数
    :return:
    """
    for q in question:
        models.ExamQuestion.objects.create(
            exam=exam,
            question=q,
            full_score=score,
        )


def create_random_exam(exam_name: str, user: UserInfo, single_num: int, multiple_num: int, judge_num: int):
    """
    创建随机考试
    :param exam_name: 考试名称
    :param user: 用户
    :param single_num: 单选题数量
    :param multiple_num: 多选题数量
    :param judge_num: 判断题数量
    :return: exam
    """
    single_question = get_random_question(QuestionTypeChoice.SINGLE, single_num)
    multiple_question = get_random_question(QuestionTypeChoice.MULTIPLE, multiple_num)
    judge_question = get_random_question(QuestionTypeChoice.JUDGE, judge_num)

    exam = models.Exam.objects.create(
        user=user,
        name=exam_name,
    )

    create_exam_question_by_type(exam, single_question, 5)
    create_exam_question_by_type(exam, multiple_question, 5)
    create_exam_question_by_type(exam, judge_question, 5)

    exam.total_score = exam.examquestion_set.all().aggregate(total_score=Sum('full_score'))['total_score']
    exam.save()

    return exam


def check_answer(question: models.Question, answer: List[models.QuestionChoice]):
    """
    检查答案
    :param question: 题目
    :param answer: 答案
    :return:
    """
    correct_answer = models.QuestionChoice.objects.filter(question=question, is_correct=True)
    if len(answer) != len(correct_answer):
        return False
    for a in answer:
        if a not in correct_answer:
            return False
    return True


def revise_exam(exam: models.Exam):
    """
    批改考试
    :param exam: 考试
    :return:
    """
    exam.submit = True

    for exam_question in exam.examquestion_set.all():
        correct = check_answer(exam_question.question, exam_question.answer.all())
        if correct:
            exam_question.score = exam_question.full_score
        else:
            exam_question.score = 0
        exam_question.save()

    exam.score = exam.examquestion_set.all().aggregate(score=Sum('score'))['score']
    exam.save()

