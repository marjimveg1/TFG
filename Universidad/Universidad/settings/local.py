from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'basedatostfg',
        'USER': 'tfg',
        'PASSWORD': '1233',
        'HOST': 'localhost',
        'PORT': ''
    }
}
