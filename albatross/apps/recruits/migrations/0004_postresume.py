# Generated by Django 3.2.9 on 2022-01-13 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220113_1626'),
        ('recruits', '0003_remove_postinfo_salary_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostResume',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, '已投递'), (1, '已查看'), (2, '已接受'), (3, '已拒绝')], default=0, verbose_name='投递简历状态')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruits.postinfo', verbose_name='岗位')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.userinfo', verbose_name='用户')),
            ],
            options={
                'verbose_name': '投递简历',
                'verbose_name_plural': '投递简历',
                'db_table': 'tb_post_resume',
            },
        ),
    ]