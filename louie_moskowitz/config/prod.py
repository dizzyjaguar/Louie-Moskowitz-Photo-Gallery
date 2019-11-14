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
