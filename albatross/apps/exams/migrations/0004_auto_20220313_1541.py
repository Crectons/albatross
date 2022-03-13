# Generated by Django 3.2.9 on 2022-03-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0003_auto_20220313_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name': '测验', 'verbose_name_plural': '测验'},
        ),
        migrations.AddField(
            model_name='examquestion',
            name='answer',
            field=models.TextField(default='[]', verbose_name='答案'),
        ),
        migrations.AlterModelTable(
            name='exam',
            table='tb_exams',
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
    ]
