# Generated by Django 3.1.7 on 2021-07-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('node_1', models.TextField(default='')),
                ('node_2', models.TextField(default='')),
                ('node_3', models.TextField(default='')),
                ('post_name', models.TextField(default='')),
                ('salary', models.TextField(default='')),
                ('requirement', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('welfare', models.TextField(default='')),
                ('company_name', models.TextField(default='')),
                ('company_info', models.TextField(default='')),
                ('location', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PostTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_father', models.TextField(default='')),
                ('name_son', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('province', models.TextField(default='')),
                ('city', models.TextField(default='')),
                ('session_key', models.TextField(default='')),
                ('avatar', models.TextField(default='')),
                ('openid', models.TextField(default='')),
                ('name', models.TextField(default='')),
                ('sex', models.IntegerField(default='')),
                ('age', models.IntegerField(default='')),
                ('phone', models.TextField(default='')),
                ('email', models.TextField(default='')),
                ('educational_experience', models.TextField(default='')),
                ('opration_experience', models.TextField(default='')),
                ('language_ability', models.TextField(default='')),
                ('personal_works', models.TextField(default='')),
            ],
        ),
    ]
