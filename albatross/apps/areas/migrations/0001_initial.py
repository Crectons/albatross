# Generated by Django 3.2.9 on 2021-11-26 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='地名')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addinfo', to='areas.areas', verbose_name='父级的行政区域id')),
            ],
            options={
                'verbose_name': '地区',
                'db_table': 'tb_areas',
            },
        ),
    ]