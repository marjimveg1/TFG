from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['tfguni.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dck30heug5gjmv',
        'USER': 'qzayzqdlvcqggh',
        'PASSWORD': '7f08c9c3808df6328b9ecc7bb2a69387259bf39e6797c724a8419fa6d55e4d69',
        'HOST': 'ec2-18-233-137-77.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
