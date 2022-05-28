"""
Django settings for attendance_tracker project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i=#62n98o_c+swyj_wujqex4#u@1fyg&)_#3z+mctm^j2eq-cr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'authapp',
    'attendanceapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
     'rest_framework',
     'django.contrib.sites',
         'corsheaders',
             'rest_framework.authtoken',
     'cloudinary_storage',
      'django.contrib.staticfiles',
    'cloudinary',
    'phonenumber_field',
     "dj_rest_auth",
    "allauth",
    "allauth.account",
   "dj_rest_auth.registration",   "allauth.socialaccount",   "allauth.socialaccount.providers.google",
]

MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CLOUDINARY_URL='cloudinary:CLOUDINARY_URL=cloudinary://695456694328799:BkmjJYC6N5XkzCMF-hMKBpqwfnE@my-tutor'

CLOUDINARY_STORAGE  = {
  'CLOUD_NAME' : 'my-tutor', 
  'API_KEY' :'695456694328799', 
  'API_SECRET' : 'BkmjJYC6N5XkzCMF-hMKBpqwfnE',

}
SOCIALACCOUNT_PROVIDERS = {
   'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
       }
    }
 }
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

SITE_ID = 1
ROOT_URLCONF = 'eng_backend.urls'
CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'authapp.myuser'
CELERY_BROKER_URL = 'amqps://gwewsfku:1Ek9hM3tes4wOaXJQ0D-YNbndmjGX2WO@sparrow.rmq.cloudamqp.com/gwewsfku'
CELERY_BROKER_Ports = ['5672']
CELERY_TIMEZONE = "Australia/Tasmania"
CELERY_TASK_TRACK_STARTED = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'eng_backend.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ]
}
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',



]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/media/'  # or any prefix you choose
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

django_heroku.settings(locals())
