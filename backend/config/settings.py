import environ
from datetime import timedelta

ROOT_DIR = environ.Path(__file__) - 2

env = environ.Env()

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'graphene_django',
    'django_extensions',
]

LOCAL_APPS = [
    'apps.users',
    'apps.trash',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEBUG = env.bool('DEBUG')
SECRET_KEY = env.str('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])
DOMAIN = env.str('DOMAIN')

EMAIL_PORT = env.int('EMAIL_PORT', default='1025')
EMAIL_HOST = env.str('EMAIL_HOST', default='mailhog')

ADMINS = [
    ('Simeon Aleksov', 'aleksov_s@outlook.com'),
]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str('POSTGRES_DB'),
        'USER': env.str('POSTGRES_USER'),
        'PASSWORD': env.str('POSTGRES_PASSWORD'),
        'HOST': 'postgres',
        'PORT': 5432,
    },
}

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

USE_TZ = True

STATIC_ROOT = str(ROOT_DIR('staticfiles'))

STATIC_URL = '/staticfiles/'

STATICFILES_DIRS = [
    str(ROOT_DIR('static')),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


MEDIA_ROOT = str(ROOT_DIR('media'))

MEDIA_URL = '/media/'


ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': STATICFILES_DIRS,
        'OPTIONS': {
            'debug': DEBUG,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]


AUTH_USER_MODEL = 'users.User'


GRAPHENE = {
    'SCHEMA': 'config.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

if DEBUG:
    GRAPHENE['MIDDLEWARE'] = [
        'graphene_django.debug.DjangoDebugMiddleware',
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ]

GRAPHQL_JWT = {
    'JWT_EXPIRATION_DELTA': timedelta(days=30),
    'JWT_AUTH_HEADER': 'authorization',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}


INSTALLED_APPS += ['raven.contrib.django.raven_compat']
RAVEN_MIDDLEWARE = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware']
MIDDLEWARE = RAVEN_MIDDLEWARE + MIDDLEWARE

SENTRY_DSN = env.str('SENTRY_DSN')
SENTRY_CLIENT = 'raven.contrib.django.raven_compat.DjangoClient'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django.security.DisallowedHost': {
            'level': 'ERROR',
            'handlers': ['console', 'sentry'],
            'propagate': False,
        },
    },
}

RAVEN_CONFIG = {
    'DSN': SENTRY_DSN
}
