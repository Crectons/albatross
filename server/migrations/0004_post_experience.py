# Generated by Django 3.1.7 on 2021-07-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_intention'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='experience',
            field=models.TextField(default=''),
        ),
    ]
