"""
Django settings for studyus_project project.

These are development settings and should not be used by a production site.
See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
"""

import os

from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# FOR DEVELOPMENT PURPOSES ONLY
SECRET_KEY = 'mvjwx1d09!(3j-m4ls7+n-kgf*^l21+c3n5atn0sfiniy-xq$4'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Demo project
    'studyus_project',

    # Installed apps used by studyus
    'account',

    # Studyus apps
    'studyus',
    'studyus.studyuser',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Required by studyus
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'studyus_project.urls'

WSGI_APPLICATION = 'studyus_project.wsgi.application'

# SQLite isn't high performance, but has native Django support.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = (
    # Required for studyus's usage of django-user-accounts.
    'account.auth_backends.EmailAuthenticationBackend',
) + global_settings.AUTHENTICATION_BACKENDS

TEMPLATE_CONTEXT_PROCESSORS = (
    # Required for studyus's usage of django-user-accounts.
    'account.context_processors.account',

    # Allows templates to access the 'request' object
    'django.core.context_processors.request',

) + global_settings.TEMPLATE_CONTEXT_PROCESSORS

# studyus required settings
ACCOUNT_EMAIL_UNIQUE = True

# This requires a user to confirm email before they can log in.
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = None

# Account related features you may wish to override.
# ACCOUNT_LOGIN_URL (Default: 'account_login')
