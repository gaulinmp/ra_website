# -*- coding: utf-8 -*-
import os

from .base import *
try:
    from .secret import *
except ImportError:
    pass

# Custom variables
PDF_ROOT = "/opt/projects/coc/files/"

ALLOWED_HOSTS = ['sub_domain.example.com', 'localhost',]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.abspath(root('../ra_website.db')),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/ra_website.django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
