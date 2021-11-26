#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'albatross.settings.dev')  # co: 不知道为啥环境变量默认写入了 albatross.settings，导致环境变量设置失败
    os.environ['DJANGO_SETTINGS_MODULE'] = 'albatross.settings.dev'  # dev 配置

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
