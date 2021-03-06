import os
from pickle import TRUE
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '-3&ciydd_*vkt93q=vasdfasdf+9!j53!ectu290_v6*$ea!_re&8=25u3'

DEBUG = True

OFFLINE = os.environ.get('IVETL_OFFLINE') == '1'

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django_cassandra_engine',
    'ivweb.app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'ivweb.app.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'ivweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'ivweb.app.context_processors.common',
                'ivweb.app.context_processors.constants',
            ],
        },
    },
]

WSGI_APPLICATION = 'ivweb.wsgi.application'

# Force HTTPS and grab the swallowed https protocol from the load balancer in a header
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

# Language, time, i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Pacific'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'app/static')

# Sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# Auth
LOGIN_URL = '/login/'

# Logging setup
LOG_ROOT = os.environ.get('IVWEB_LOG_ROOT', '/var/log/ivweb')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_ROOT, 'app.log'),
            'formatter': 'verbose'
        },
        'tools_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_ROOT, 'tools.log'),
            'formatter': 'verbose'
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'ivweb': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
        'simplecache': {
            'handlers': ['file'],
            # 'level': 'WARNING',  # change to DEBUG to see all the cache activity
            'level': 'DEBUG',
        },
        'django.db.backends': {
            'handlers': ['null'],
            'propagate': False,
            'level': 'DEBUG',
        },
    }
}
