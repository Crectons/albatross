"""
WSGI config for albatross project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

import sys
sys.path.append("/usr/lib/python3.6/site-packages")

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'albatross.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'albatross.settings.prod'

application = get_wsgi_application()
