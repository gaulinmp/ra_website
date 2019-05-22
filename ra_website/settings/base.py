# -*- coding: utf-8 -*-
import os
import sys

DEBUG = False

# PATH vars
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = lambda *x: os.path.join(BASE_DIR, *x)

sys.path.insert(0, root('apps'))

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # 'registration', # I don't like this up here, but it's in the docs
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'html_checker',
]

INSTALLED_APPS += PROJECT_APPS

# MIDDLEWARE_CLASSES = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ra_website.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ra_website.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ra_website.db',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'America/Denver'
USE_I18N = False
USE_L10N = True
USE_TZ = True

LOGIN_URL = 'login/'
LOGOUT_URL = 'logout/'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# Additional locations of static files
STATICFILES_DIRS = (
    root('static'),
)
STATIC_ROOT = '/opt/static/ra_website/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            root('templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                # 'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                'django.template.context_processors.static',
                # 'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'ra_website.context_processors.google_analytics',
                'ra_website.context_processors.get_current_next',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
            'libraries': {
                'auth_tags' : 'ra_website.templatetags.auth_tags',
            },
        },
    }
]

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

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
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}

# Registration functionality
# using django-registration-redux
INCLUDE_AUTH_URLS = True
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_EMAIL_HTML = False
REGISTRATION_AUTO_LOGIN = True
LOGIN_URL = 'accounts/login/'
LOGOUT_URL = 'accounts/logout/'


DOC_ROOT = root('files')
