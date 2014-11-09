"""
Django settings for siscupos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kb*u-$(cout=&=b20*h@lewq3ami^4q&v9!13e!pa$v%826#*n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*','siscupos-dev.herokuapp.com']

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'siscupos'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import dj_database_url
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd8iv5ac7d1jos6',
        'USER': 'kpbaqcwlfpqkgw',
        'PASSWORD': '4KLEgGfQDTQN2qgVYUo6DJfXiy',
        'HOST': 'ec2-23-23-183-5.compute-1.amazonaws.com',
        'PORT': '5432',
    }
    #'default' :  dj_database_url.config()
}



#TEST_RUNNER = 'siscupos.test.test_suite_runner.HerokuTestSuiteRunner'
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_RUNNER = 'siscupos.test.test_suite_runner.NoseTestSuiteRunner'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
 )

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

#TEMPLATE_CONTEXT_PROCESSORS = (
 #   'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.debug',
    #'django.core.context_processors.i18n',
    #'django.core.context_processors.media',
    #'django.core.context_processors.static',
    #'django.core.context_processors.tz',
    #'django.contrib.messages.context_processors.messages',
 #   'django.core.context_processors.request',
#)
#MEDIA_ROOT = join(BASE_DIR, 'media')
#MEDIA_URL = '/media/'
#MAX_UPLOAD_SIZE = 20971520 # 20MB
#CONTENT_TYPES = ['application/pdf', 'image/jpeg', 'image/png'] # .pdf, .jpeg and .png


SUIT_CONFIG = {
    'ADMIN_NAME': 'Siscupos Admin'
}