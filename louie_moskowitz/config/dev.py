from .base import *
import logging

DEBUG = True

logging.basicConfig(level=logging.DEBUG)

ADMINS = ['localhost']

INSTALLED_APPS = ['whitenoise.runserver_nostatic'] + INSTALLED_APPS
