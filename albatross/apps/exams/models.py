from django.db import models

from albatross.utils.choices import QuestionTypeChoice


class Question(models.Model):
    """
    问题
    """
    content = models.TextField(verbose_name='问题内容')
    type = models.IntegerField(choices=QuestionTypeChoice.choices, default=QuestionTypeChoice.SINGLE, verbose_name='问题类型')
    is_vip = models.BooleanField(default=False, verbose_name='是否为VIP问题')

    class Meta:
        app_label = 'exams'
        db_table = 'tb_questions'
        verbose_name = '问题'
        verbose_name_plural = verbose_name


class QuestionChoice(models.Model):
    """
    问题选项
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='问题')
    content = models.TextField(verbose_name='选项内容')
    is_correct = models.BooleanField(default=False, verbose_name='是否正确')

    class Meta:
        app_label = 'exams'
        db_table = 'tb_questions_choices'
        verbose_name = '问题选项'
        verbose_name_plural = verbose_name


class QuestionAnswer(models.Model):
    """
    问题答案
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='问题')
    content = models.TextField(verbose_name='答案内容')

    class Meta:
        app_label = 'exams'
        db_table = 'tb_questions_answers'
        verbose_name = '问题答案'
        verbose_name_plural = verbose_name


class ExamQuestion(models.Model):
    """
    试卷题目
    """
    exam = models.ForeignKey('Exam', on_delete=models.CASCADE, verbose_name='试卷')
    question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name='问题')
    score = models.IntegerField(default=0, verbose_name='分数')

    class Meta:
        app_label = 'exams'
        db_table = 'tb_exams_questions'
        verbose_name = '试卷题目'
        verbose_name_plural = verbose_name


class Exam(models.Model):
    """
    试卷
    """
    user = models.ForeignKey('users.UserInfo', on_delete=models.CASCADE, verbose_name='用户')
    name = models.CharField(max_length=100, verbose_name='试卷名称')
    score = models.IntegerField(default=0, verbose_name='总分')
    submit = models.BooleanField(default=False, verbose_name='是否提交')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
