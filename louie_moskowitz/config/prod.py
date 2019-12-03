from .base import *
import logging

DEBUG = False

logging.basicConfig(level=logging.INFO)

ALLOWED_HOSTS = ['louie-gallery.herokuapp.com']

DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# A comma-separated list of email addresses for admins
ADMIN_EMAILS = os.environ.get('ADMIN_EMAILS')
if ADMIN_EMAILS:
    ADMINS = [admin.strip() for admin in ADMIN_EMAILS.split(',')]


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

AWS_AUTO_CREATE_BUCKET = True

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# AWS_LOCATION = 'static'
