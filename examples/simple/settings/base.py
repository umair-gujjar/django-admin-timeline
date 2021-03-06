# Django settings for example project.
import os
import sys

from nine import versions

from .core import PROJECT_DIR, gettext


DEBUG = False
DEBUG_TOOLBAR = False
TEMPLATE_DEBUG = DEBUG
DEV = False

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR(os.path.join('..', '..', 'db', 'example.db')),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_DIR(os.path.join('..', '..', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_DIR(os.path.join('..', '..', 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_DIR(os.path.join('..', '..', 'media', 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '6sf18c*w971i8a-m^1coasrmur2k6+q5_kyn*)s@(*_dk5q3&r'


try:
    from .local_settings import DEBUG_TEMPLATE
except Exception as err:
    DEBUG_TEMPLATE = False


if versions.DJANGO_GTE_1_10:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 'APP_DIRS': True,
            'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
            'OPTIONS': {
                'context_processors': [
                    "django.template.context_processors.debug",
                    'django.template.context_processors.request',
                    "django.contrib.auth.context_processors.auth",
                    # "django.core.context_processors.i18n",
                    # "django.core.context_processors.media",
                    # "django.core.context_processors.static",
                    # "django.core.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    # 'django.template.loaders.eggs.Loader',
                ],
                'debug': DEBUG_TEMPLATE,
            }
        },
    ]
elif versions.DJANGO_GTE_1_8:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            # 'APP_DIRS': True,
            'DIRS': [PROJECT_DIR(os.path.join('..', 'templates'))],
            'OPTIONS': {
                'context_processors': [
                    "django.contrib.auth.context_processors.auth",
                    "django.template.context_processors.debug",
                    "django.template.context_processors.i18n",
                    "django.template.context_processors.media",
                    "django.template.context_processors.static",
                    "django.template.context_processors.tz",
                    "django.contrib.messages.context_processors.messages",
                    "django.template.context_processors.request",
                ],
                'loaders': [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    # 'django.template.loaders.eggs.Loader',
                ],
                'debug': DEBUG_TEMPLATE,
            }
        },
    ]
else:
    TEMPLATE_DEBUG = DEBUG_TEMPLATE

    # List of callables that know how to import templates from various
    # sources.
    TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',

    ]

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
    )

    TEMPLATE_DIRS = (
        # Put strings here, like "/home/html/django_templates" or
        # "C:/www/django/templates".
        # Always use forward slashes, even on Windows.
        # Don't forget to use absolute paths, not relative paths.
        PROJECT_DIR(os.path.join('..', 'templates')),
    )

# # List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
# )

_MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

# TEMPLATE_DIRS = (
#     # Put strings here, like "/home/html/django_templates" or
#     # "C:/www/django/templates".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     PROJECT_DIR('templates'),
# )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'admin_timeline',  # admin-timeline

    'foo',  # Example app to generate test data
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '\n%(levelname)s %(asctime)s [%(pathname)s:%(lineno)s] '
                      '%(message)s'
        },
        'simple': {
            'format': '\n%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'django_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR(
                os.path.join('..', '..', 'logs', 'django.log')
            ),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
        'admin_timeline_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_DIR(
                os.path.join('..', '..', 'logs', 'admin_timeline.log')
            ),
            'maxBytes': 1048576,
            'backupCount': 99,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'admin_timeline': {
            'handlers': ['console', 'admin_timeline_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}


# Do not put any settings below this line
try:
    from .local_settings import *
except:
    pass

# Make the `django-admin-timeline` package available without installation.
if DEV:
    admin_timeline_source_path = os.environ.get(
        'ADMIN_TIMELINE_SOURCE_PATH', 'src'
    )
    sys.path.insert(0, os.path.abspath(admin_timeline_source_path))

if DEBUG and DEBUG_TOOLBAR:
    # debug_toolbar
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
        'debug_toolbar',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

# Avoid code duplication
if versions.DJANGO_GTE_1_10:
    MIDDLEWARE = _MIDDLEWARE
else:
    MIDDLEWARE_CLASSES = _MIDDLEWARE
