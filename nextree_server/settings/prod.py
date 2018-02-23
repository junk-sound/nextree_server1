import os
from .common import *

DEBUG = True
ALLOWED_HOSTS = ['13.125.173.238']

STATIC_ROOT = os.path.join(BASE_DIR, "..", "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testdb5',
        'USER': 'junksound',
        'PASSWORD': 'wekimeki',
        'HOST': 'localhost',
	},
}
