# -*- coding: utf-8 -*-
import os

from .base import *
try:
    from .secret import *
except ImportError:
    pass

DEBUG = True
SECRET_KEY = "What secret key bruh?"


GOOGLE_ANALYTICS_PROPERTY_ID = ''
GOOGLE_ANALYTICS_DOMAIN = ''

# Debug toolbar
INSTALLED_APPS += ("debug_toolbar", )
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = ['127.0.0.1', 'localhost',]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
