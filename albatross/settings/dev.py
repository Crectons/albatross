from .base import *

# local test mysql server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'albatross',
        'USER': 'albatross',
        'PASSWORD': 'albatross',
        'HOST': '192.168.239.128',
        # 'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}