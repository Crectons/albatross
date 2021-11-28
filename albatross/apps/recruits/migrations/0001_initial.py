# Generated by Django 3.2.9 on 2021-11-28 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTree',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='岗位分类名')),
                ('type', models.IntegerField(choices=[(1, '一级分类'), (2, '二级分类'), (3, '三级分类')], verbose_name='岗位分类类型')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='recruits.posttree', verbose_name='父级分类')),
            ],
            options={
                'verbose_name': '岗位分类',
                'verbose_name_plural': '岗位分类',
                'db_table': 'tb_post_tree',
            },
        ),
        migrations.CreateModel(
            name='PostInfo',
            fields=[
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('pid', models.AutoField(primary_key=True, serialize=False, verbose_name='岗位ID')),
                ('post_name', models.CharField(default='', max_length=100, verbose_name='岗位名称')),
                ('salary_low', models.IntegerField(default=0, verbose_name='薪资下限')),
                ('salary_high', models.IntegerField(default=0, verbose_name='薪资上限')),
                ('salary_type', models.IntegerField(choices=[(0, '未知'), (1, '月薪'), (2, '年薪')], default=0, verbose_name='薪资类型')),
                ('education', models.IntegerField(choices=[(0, '未知'), (1, '不限'), (2, '小学'), (3, '初中'), (4, '高中'), (5, '中专'), (6, '大专'), (7, '本科'), (8, '硕士'), (9, '博士')], default=1, verbose_name='学历要求')),
                ('experience', models.CharField(default='', max_length=100, verbose_name='工作经验')),
                ('description', models.TextField(default='', verbose_name='岗位介绍')),
                ('welfare', models.TextField(default='', verbose_name='福利')),
                ('score', models.IntegerField(default=0, verbose_name='岗位评分')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.companyinfo', verbose_name='公司')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='areas.areas', verbose_name='办公地点')),
                ('node_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node_1_related', to='recruits.posttree', verbose_name='一级岗位')),
                ('node_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node_2_related', to='recruits.posttree', verbose_name='二级岗位')),
                ('node_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='node_3_related', to='recruits.posttree', verbose_name='三级岗位')),
            ],
            options={
                'verbose_name': '岗位信息',
                'verbose_name_plural': '岗位信息',
                'db_table': 'tb_post_info',
            },
        ),
    ]
