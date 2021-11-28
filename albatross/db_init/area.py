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


from areas.models import Areas


for province in Areas.objects.filter(pid=None):
    province.display = province.name
    province.save()
    for city in Areas.objects.filter(pid=province.id):
        city.display = f'{province.name}-{city.name}'
        city.save()
        for district in Areas.objects.filter(pid=city.id):
            district.display = f'{province.name}-{city.name}-{district.name}'
            district.save()
