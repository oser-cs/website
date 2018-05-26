"""Production settings."""

import os

from celery.schedules import crontab

from aws.conf import *

from .common import *

DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = [
    'localhost',
    'oser-backend.herokuapp.com',
    'oser-backend-staging.herokuapp.com',
    'oser-cs.fr',
]

# Security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

# Mails
MAILS_ENABLED = True
SENDGRID_SANDBOX_MODE_IN_DEBUG = os.environ.get(
    'SENDGRID_SANDBOX_MODE_IN_DEBUG', True)

# Celery settings

CELERY_BEAT_SCHEDULE = {
    # Clean media files every day at 22:00
    'clean-media-every-hour': {
        'task': 'core.tasks.clean_media',
        'schedule': crontab(minute='0', hour='22'),
    },
}
