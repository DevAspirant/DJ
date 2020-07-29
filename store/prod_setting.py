import os

from .settings import *

import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ['https://marvelous-everglades-50690.herokuapp.com/']

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}