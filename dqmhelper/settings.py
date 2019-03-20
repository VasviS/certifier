"""
Django settings for dqmhelper project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default="*o5*!8r8_nkv5=81dddg+y12hm7#_pw$88g8v218*tpn1g0s9=")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    config('DJANGO_ALLOWED_HOSTS', default='localhost'),
    'tkdqmdoctor.web.cern.ch',
    'dev-tkdqmdoctor.web.cern.ch',
    'test-tkdqmdoctor.web.cern.ch',
    '127.0.0.1',
    "test-tracker-certifer.web.cern.ch",
]

# Application definition

INSTALLED_APPS = [
    "users.apps.UsersConfig",
    "plot.apps.PlotConfig",
    "analysis.apps.AnalysisConfig",
    "home.apps.HomeConfig",
    "certifier.apps.CertifierConfig",
    "oms.apps.OmsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'rest_framework',
    'bootstrap3',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.cern',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dqmhelper.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = "dqmhelper.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DJANGO_DATABASE_ENGINE', default=''),
        'NAME': config('DJANGO_DATABASE_NAME', default=''),
        'USER': config('DJANGO_DATABASE_USER', default=''),
        'PASSWORD': config('DJANGO_DATABASE_PASSWORD', default=''),
        'HOST': config('DJANGO_DATABASE_HOST', default=''),
        'PORT': config('DJANGO_DATABASE_PORT', default=''),
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'home/static'))
STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi/static')

#AUTH_USER_MODEL = "certifier.User"

EMAIL_HOST = config('DJANGO_EMAIL_HOST', default='localhost')
EMAIL_PORT = config('DJANGO_EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_USER = config('DJANGO_EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('DJANGO_EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('DJANGO_EMAIL_USE_TLS', default=False, cast=bool)
SERVER_EMAIL = config('DJANGO_SERVER_EMAIL', default='root@localhost')
