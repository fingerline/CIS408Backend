DEBUG = True

ALLOWED_HOSTS = []
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cis408', 
        'USER': 'postgres', 
        'PASSWORD': 'r0ttenB4nana',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}