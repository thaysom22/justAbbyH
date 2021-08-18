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

# SECURITY INFO: SECRET_KEY different in production
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in env

ALLOWED_HOSTS = ['just-abby-h.herokuapp.com', 'localhost']

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
    'crispy_forms',
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
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ],
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

WSGI_APPLICATION = 'justAbbyH.wsgi.application'


# DATABASE AND MIGRATIONS
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

USE_PRODUCTION_DATABASE = 'DATABASE_URL' in env
if USE_PRODUCTION_DATABASE:
    # use postgres remote
    DATABASES = {
        'default': dj_database_url.parse(env('DATABASE_URL')),
    }
    # separate stories app migrations production/development packages
    MIGRATION_MODULES = {
        'stories': 'stories.migrations_production',
    }
else:
    # use sqlite locally
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    MIGRATION_MODULES = {
        'stories': 'stories.migrations_development',
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

# Login and logout redirect urls

LOGIN_REDIRECT_URL = 'stories'
LOGOUT_REDIRECT_URL = 'index'

# Stripe

SUBSCRIPTION_COST = 5  # subscription cost
STRIPE_CURRENCY = 'usd'
STRIPE_PUBLIC_KEY = env('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = env('STRIPE_WH_SECRET')  # different for dev/prod hosts

# STATIC AND MEDIA STORAGE

# search this folder in addition to static files
# within each app when 'collect static' command is run
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

USE_AWS = 'USE_AWS' in env
if USE_AWS:
    # production settings
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_ACL = None

    # cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # bucket config
    AWS_STORAGE_PUBLIC_BUCKET_NAME = env('AWS_STORAGE_PUBLIC_BUCKET_NAME')
    AWS_STORAGE_PRIVATE_BUCKET_NAME = env('AWS_STORAGE_PRIVATE_BUCKET_NAME')

    # domain config
    AWS_S3_CUSTOM_PUBLIC_DOMAIN = f"{AWS_STORAGE_PUBLIC_BUCKET_NAME}.s3.amazonaws.com"
    AWS_S3_CUSTOM_PRIVATE_DOMAIN = f"{AWS_STORAGE_PRIVATE_BUCKET_NAME}.s3.amazonaws.com"

    # static files in production
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'  # where 'collect static' command will put static files in production
    STATICFILES_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_PUBLIC_DOMAIN}/{STATICFILES_LOCATION}/'

    # media files in production
    MEDIAFILES_PUBLIC_LOCATION = 'media/public'   
    MEDIAFILES_PRIVATE_LOCATION = 'media/private'    
    MEDIA_PUBLIC_URL = f'https://{AWS_S3_CUSTOM_PUBLIC_DOMAIN}/{MEDIAFILES_PUBLIC_LOCATION}/'
    MEDIA_PRIVATE_URL = f'https://{AWS_S3_CUSTOM_PRIVATE_DOMAIN}/{MEDIAFILES_PRIVATE_LOCATION}/'
    PUBLIC_FILE_STORAGE = 'custom_storages.PublicFileStorage'
    PRIVATE_FILE_STORAGE = 'custom_storages.PrivateFileStorage'
else:
    # static and media in development
    STATIC_URL = '/static/'  # url prefix for referring to static files in development
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # where 'collect static' command will put static files locally
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

# EMAIL
USE_SMTP = 'USE_SMTP' in env
if USE_SMTP:
    # use gmail smtp server    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'  # OR 'smtp-relay.sendinblue.com'
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # using app password with 2FA
    DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')
    CURRENT_SITE_DOMAIN = None  # webhook handler will get domain from request object
else:
    # print email to terminal instead of sending
    CURRENT_SITE_DOMAIN = env('CURRENT_SITE_DOMAIN')  # from $gp url 8000
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'justabbyh.stories@example.com'
