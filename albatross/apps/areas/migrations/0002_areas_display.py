# Generated by Django 3.2.9 on 2021-11-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='areas',
            name='display',
            field=models.CharField(default='', max_length=150, verbose_name='显示名称'),
            preserve_default=False,
        ),
    ]