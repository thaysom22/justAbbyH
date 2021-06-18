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
print(env('DEVELOPMENT'))

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

if 'DATABASE_URL' in env:
    print('using production database')  # TEST
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL')),
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

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
if 'USE_AWS' in env:
    # bucket config
    AWS_STORAGE_BUCKET_NAME = 'just-abby-h'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    # static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    STATICFILES_LOCATION = 'static'
    MEDIAFILES_LOCATION = 'media'

    # override static and media urls in production
    

