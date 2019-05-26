import os

BASE_DIRECTION = os.path.dirname(os.path.dirname(os.path.abspath(_file_)))

SECRET_KEY = ''

INSTALLED_APPS = [

]

MIDDLEWARE = [

]

ROOT_URLCONF = ''

TEMPLATES = [
    {

    }
]

environment = 'prod'

if environment == 'dev':
    DEBUG = True
    ALLOWED_HOST = []
    DATABASE = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': ''
        }
    }

EMAIL_BACKEND = ''

EMAIL_USER_SSL = True
EMAIL_HOST =''
EMAIL_PORT =''
EMAIL_USER =''
EMAIL_CERTIFICATION =''
EMAIL_SEND_FROM = ''
