"""
Django settings for mm_trainer_django project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wghz%yy(70ek=9$4%0c&s=u5o6&$6(-lld*$gvyfhgfto#$m3k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

isLocalEnv = os.environ.get('LOCALDEV')

# This indicates that app is run on macos and developer probably wants to run in local dev mode
isPubSubSocketRender = os.environ.get('Apple_PubSub_Socket_Render')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SITE_ID = 2
CORS_ORIGIN_ALLOW_ALL = True

if isPubSubSocketRender is not None and isLocalEnv is None:
    print("MM-SERVICE-WARN: Looks like you're trying to run the app for local dev, but you haven't indicated as such.")
    print("MM-SERVICE-WARN: Stop application now and set the env variable LOCALDEV to '1'.")
    print("MM-SERVICE-WARN: If using Pycharm, this can be done through:")
    print("MM-SERVICE-WARN: Run -> Edit Configuration -> Environment Variables.")

elif isLocalEnv is not None and int(isLocalEnv) == 1:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    print("Configuration settings for local development environment...", file=sys.stderr)
    print("Mental Math service media root: ", MEDIA_ROOT, file=sys.stderr)
    print("Path to mental math service media root:", MEDIA_URL, file=sys.stderr)

else:
    MEDIA_ROOT = '/mnt/nfs/var/www/mmservicemedia'
    MEDIA_URL = 'http://cdn.mental-math.com/'
    print("Configuring settings for QA environment...", file=sys.stderr)
    print("Mental Math service media root: ", MEDIA_ROOT, file=sys.stderr)
    print("Path to media: ", MEDIA_URL, file=sys.stderr)


# Application definition

INSTALLED_APPS = [
    'mm_trainer_rest_api.apps.MmTrainerRestApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mm_trainer_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mm_trainer_django.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'PAGE_SIZE': 10,
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination'
}

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'mm_trainer_rest_api.serializers.TokenSerializer',
}

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mentalmathdb',
        'USER': 'mentalmathpgadmin',
        'PASSWORD': '[%3e}A9?r3F7',
        'HOST': 'localhost',
        'PORT': '',
        # consider adding ALLOWED_HOSTS property as well to filter access to db by domain and or subdomain
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
#EMAIL_BACKEND = 'django.core.backends.console.EmailBackend'

# if you're running a local SMTP server via: python3 -m aiosmtpd -n
# THen enable the below env vars:
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 8025

#ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
#ACCOUNT_EMAIL_REQUIRED = True
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mmtrainerhelpdesk'
EMAIL_HOST_PASSWORD = '6);%3un39J}T'
EMAIL_PORT = 587
ACCOUNT_ADAPTER = 'mm_trainer_rest_api.adapter.MMAccountAdapter'
URL_FRONT = 'http://localhost:4200/'