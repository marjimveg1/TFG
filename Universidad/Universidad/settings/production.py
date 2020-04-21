from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['tfguni.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd495oj224n1p7',
        'USER': 'vexljkjdcvqroy',
        'PASSWORD': '981ea66a58891cf881c056f1377df4ddb6e028ca3300af1dcd635cfdd82ae8de',
        'HOST': 'ec2-52-71-85-210.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
