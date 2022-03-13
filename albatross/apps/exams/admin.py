from django.contrib import admin
from . import models


class QuestionChoiceInline(admin.TabularInline):
    model = models.QuestionChoice
    extra = 0
    verbose_name = '问题选项'
    verbose_name_plural = verbose_name


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_per_page = 20  # 每页显示条数

    inlines = [QuestionChoiceInline]
