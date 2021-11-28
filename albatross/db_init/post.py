"""
该文件用于 python 脚本的 CRUD 操作
"""
import os
import sys
import django
import json

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '../../../..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'albatross.settings.dev'

django.setup()

from recruits.models import PostTree
from recruits.models import PostInfo
from areas.models import Areas
from companies.models import CompanyInfo
from albatross.utils.choices import EducationChoice

data = json.load(open('server_post.json', 'r', encoding='utf-8'))['RECORDS']

for item in data:
    if item['post_name'] == '':
        continue
    if item['salary'] == '':
        continue
    if '天' in item['salary'] or '以下' in item['salary']:
        continue

    if item['node_3'] == '创意设计':
        item['node_3'] = '设计'
    if item['node_3'] == '物流':
        item['node_3'] = '物流销售'

    if '打字' in item['node_3']:
        item['node_3'] = '电脑操作/打字/录入员'

    node_3 = PostTree.objects.filter(type=3).filter(name=item['node_3'])
    if node_3.count() == 0:
        pass
    else:
        node_3 = node_3[0]

    node_2 = PostTree.objects.filter(id=node_3.father_id)[0]
    node_1 = PostTree.objects.filter(id=node_2.father_id)[0]

    post_name = item['post_name']



    salary_list = item['salary'].split('/')
    if salary_list[1] == '月':
        salary_type = 1
    elif salary_list[1] == '年':
        salary_type = 2
    else:
        pass

    if salary_list[0][-1] == '万':
        salary_unit = 10000
    elif salary_list[0][-1] == '千':
        salary_unit = 1000
    else:
        pass
    salary_list[0] = salary_list[0][:-1]
    salary_range = salary_list[0].split('-')
    salary_min = int(float(salary_range[0]) * salary_unit)
    salary_max = int(float(salary_range[1]) * salary_unit)
    if item['requirement'] == "":
        item['requirement'] = '不限'
    requirement = EducationChoice.labels.index(item['requirement'])
    description = item['description']
    welfare = item['welfare']
    experience = item['experience']

    company = CompanyInfo.objects.filter(name=item['company_name'])
    if company.count() == 0:
        company = CompanyInfo(
            name=item['company_name'],
            info=item['company_info'],
        )
        company.save()
    else:
        company = company[0]

    location_str = item['location'].split('-')[-1]
    if location_str == '东湖新技术产业开发区':
        location_str = '东湖新技术开发区'
    if location_str == '武汉经济开发区':
        location_str = '武汉'
    location = Areas.objects.filter(name__startswith=location_str)

    if location.count() == 0:
        pass
    else:
        location = location[0]

    post_info = PostInfo(
        node_1=node_1,
        node_2=node_2,
        node_3=node_3,
        post_name=post_name,
        salary_min=salary_min,
        salary_max=salary_max,
        salary_type=salary_type,
        requirement=requirement,
        description=description,
        welfare=welfare,
        experience=experience,
        company=company,
        location=location,
    )

    post_info.save()

    pass

pass