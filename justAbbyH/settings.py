"""
Django settings for justAbbyH project.
"""

from pathlib import Path
import os

import environ
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# get environment variables using django-environ
env = environ.Env(DEVELOPMENT=(bool, False))  # 'true' evaluates to True
env_file = os.path.join(BASE_DIR, ".env")
environ.Env.read_env(env_file)

# SECURITY INFO: development and production env have different SECRET_KEY
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEVELOPMENT')

ALLOWED_HOSTS = ['just-abby-h.herokuapp.com', 'localhost']  # ADD DOMAIN NAME FOR DEPLOYED SITE

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'stories',
    'subscribe',

    # other
    'storages',
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

ROOT_URLCONF = 'justAbbyH.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.static',  # removes need for 'load static' in templates
            ],
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

WSGI_APPLICATION = 'justAbbyH.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# if 'DATABASE_URL' in env:
if True:
    print('using production database')  # TEST
    DATABASES = {
        # 'default': dj_database_url.parse(env('DATABASE_URL')),
        'default': dj_database_url.parse("postgres://uzvtsjjoblskbs:1c545089a568e6144f3e5690acedce4d88aa7b3022892720a65893c64a83e7dc@ec2-54-87-34-201.compute-1.amazonaws.com:5432/d86blkjgbcjvvt"),
    }
else:
    print('using development database')  # TEST
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login and logout redirects

LOGIN_REDIRECT_URL = 'stories'
LOGOUT_REDIRECT_URL = 'index'

# Stripe and payments

SUBSCRIPTION_COST = 10.00  # one-time subscription cost in usd
STRIPE_CURRENCY = 'usd'

STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')


# AWS

USE_AWS = 'USE_AWS' in env

# if 'USE_AWS':
if True:
    # production settings
    print("Using S3 storage")  # TEST

    AWS_S3_REGION_NAME = 'us-east-1'
    # AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    # AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_ACCESS_KEY_ID = "AKIAYFWDKLXUF4OLBRTO"  # TEST
    AWS_SECRET_ACCESS_KEY = "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"  # TEST

    # cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # bucket config
    AWS_STORAGE_PUBLIC_BUCKET_NAME = 'just-abby-h-public'
    AWS_STORAGE_PRIVATE_BUCKET_NAME = 'just-abby-h-private'

    # domain config
    AWS_S3_CUSTOM_PUBLIC_DOMAIN = f"{AWS_STORAGE_PUBLIC_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_CUSTOM_PRIVATE_DOMAIN = f"{AWS_STORAGE_PRIVATE_BUCKET_NAME}.s3.amazonaws.com"

    # static files in production
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_PUBLIC_DOMAIN}/{STATICFILES_LOCATION}/'

    # media files in production
    MEDIAFILES_PUBLIC_LOCATION = 'media/public'   
    MEDIAFILES_PRIVATE_LOCATION = 'media/private'    
    MEDIA_PUBLIC_URL = f'https://{AWS_S3_CUSTOM_PUBLIC_DOMAIN}/{MEDIAFILES_LOCATION}/'
    MEDIA_PRIVATE_URL = f'https://{AWS_S3_CUSTOM_PRIVATE_DOMAIN}/{MEDIAFILES_LOCATION}/'
    PUBLIC_FILE_STORAGE = 'custom_storages.PublicFileStorage'
    PRIVATE_FILE_STORAGE = 'custom_storages.PrivateFileStorage'
    
    
else:
    # development settings
    print("Using default local storage")  # TEST

    # static and media in development
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)