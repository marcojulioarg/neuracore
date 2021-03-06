"""
Django settings for AngelHack project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0@rbe3)ob_ec-!k8cz=(-!ga#a#bv3xhwtgrv@739rphmbf1)6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apis',
    'djasana',
    'rest_framework',
    'django_slack',
    'django_slack_oauth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AngelHack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'AngelHack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'neuracore',
        'USER': 'neuracore',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = 'localhost:8080:/project/selection.html'

# Asana API

ASANA_CLIENT_ID = '381361399383749'
ASANA_CLIENT_SECRET = '4bda78666ff91b75ae8bf4c65b3ac604'
ASANA_OAUTH_REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
ASANA_ACCESS_TOKEN = '0/3408e747301656ea8afede6c866986c7'
ASANA_AUTHORIZATION_ENDPOINT = 'https://app.asana.com/-/oauth_authorize?response_type=code&client_id=381361399383749&'\
                               'redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Fauth%2Fasana%2Fcallback&state=<STATE_PARAM>'
DJASANA_WEBHOOK_URL = 'https://localhost:8000/djasana/webhooks/'

# Slack API
SLACK_CLIENT_ID = '167706886868.209881113123'
SLACK_CLIENT_SECRET = '953205db43b5bd1c8571e71cb61140fe'
SLACK_VERIFICATION_TOKEN = 'SLTLy841ZdCdFeymYbllN4aV'
SLACK_SCOPE = 'admin,identify,' \
              'channels:write, channels:read, chat:write:bot,' \
              'chat:write:user,emoji:read,files:read,files:write:user,' \
              'groups:read,groups:write, usergroups:read, usergroups:write,' \
              'users.profile:read, users.profile:write,users:read,users:write'
SLACK_AUTHORIZATION_URL = 'https://slack.com/oauth/authorize'
SLACK_OAUTH_ACCESS_URL = 'https://slack.com/api/oauth.access'
SLACK_REDIRECT_URI = 'https://localhost:8000/neuracore'

# Team Viewer API

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
