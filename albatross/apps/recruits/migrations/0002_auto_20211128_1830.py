# Generated by Django 3.2.9 on 2021-11-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postinfo',
            name='score',
        ),
        migrations.AddField(
            model_name='postinfo',
            name='priority',
            field=models.BooleanField(default=False, verbose_name='优先推荐'),
        ),
        migrations.AddField(
            model_name='postinfo',
            name='recommend',
            field=models.IntegerField(default=0, verbose_name='推荐指数'),
        ),
    ]
