#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'albatross.setting.dev')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'albatross.settings_dev'

    checkLogs()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def checkLogs():
    if (not os.path.exists('./logs')) or (not os.path.isdir('./logs')):
        os.mkdir('./logs')
        open('./logs/all.log', 'w').close()
        open('./logs/django.log', 'w').close()
        open('./logs/oauth.log', 'w').close()
        open('./logs/request.log', 'w').close()
        open('./logs/server.log', 'w').close()
        open('./logs/test.log', 'w').close()

if __name__ == '__main__':
    main()
