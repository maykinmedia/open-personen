import os

# Django-hijack (and Django-hijack-admin)
from django.urls import reverse_lazy

from sentry_sdk.integrations import DidNotEnable, django, redis
from vng_api_common.conf.api import *  # noqa - imports white-listed

try:
    from sentry_sdk.integrations import celery
except DidNotEnable:  # no celery in this proejct
    celery = None

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
DJANGO_PROJECT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir)
)
BASE_DIR = os.path.abspath(
    os.path.join(DJANGO_PROJECT_DIR, os.path.pardir, os.path.pardir)
)

#
# Core Django settings
#
SITE_ID = os.getenv("SITE_ID", default=1)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "openpersonen"),
        "USER": os.getenv("DB_USER", "openpersonen"),
        "PASSWORD": os.getenv("DB_PASSWORD", "openpersonen"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", 5432),
    }
}

# in memory cache and django-axes don't get along.
# https://django-axes.readthedocs.io/en/latest/configuration.html#known-configuration-problems
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
    # https://github.com/jazzband/django-axes/blob/master/docs/configuration.rst#cache-problems
    "axes_cache": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    },
}

SOLO_CACHE = "default"

# Application definition

INSTALLED_APPS = [
    # Note: contenttypes should be first, see Django ticket #10827
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    # Note: If enabled, at least one Site object is required
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # django-admin-index
    "django_admin_index",
    "ordered_model",
    # Optional applications.
    "django.contrib.admin",
    # 'django.contrib.admindocs',
    # 'django.contrib.humanize',
    # 'django.contrib.sitemaps',
    # External applications.
    "axes",
    "vng_api_common",  # before drf_yasg to override the management command
    "drf_yasg",
    "rest_framework",
    "rest_framework.authtoken",
    "sniplates",
    "hijack",
    "compat",  # Part of hijack
    "hijack_admin",
    "solo",
    # Project applications.
    "openpersonen.accounts",
    "openpersonen.api",
    "openpersonen.utils",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # 'django.middleware.locale.LocaleMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "axes.middleware.AxesMiddleware",
]

ROOT_URLCONF = "openpersonen.urls"

# List of callables that know how to import templates from various sources.
RAW_TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    # 'admin_tools.template_loaders.Loader',
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(DJANGO_PROJECT_DIR, "templates"),
            os.path.join(DJANGO_PROJECT_DIR, "api/request_templates"),
            os.path.join(DJANGO_PROJECT_DIR, "api/tests/response_templates"),
        ],
        "APP_DIRS": False,  # conflicts with explicity specifying the loaders
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "openpersonen.utils.context_processors.settings",
            ],
            "loaders": RAW_TEMPLATE_LOADERS,
        },
    },
]

WSGI_APPLICATION = "openpersonen.wsgi.application"

# Database: Defined in target specific settings files.
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "nl-nl"

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

# Translations
LOCALE_PATHS = (os.path.join(DJANGO_PROJECT_DIR, "conf", "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Additional locations of static files
STATICFILES_DIRS = (os.path.join(DJANGO_PROJECT_DIR, "static"),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
FILE_UPLOAD_PERMISSIONS = 0o644

FIXTURE_DIRS = (os.path.join(DJANGO_PROJECT_DIR, "fixtures"),)

DEFAULT_FROM_EMAIL = "openpersonen@example.com"
EMAIL_TIMEOUT = 10

LOGGING_DIR = os.path.join(BASE_DIR, "log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(name)s %(module)s %(process)d %(thread)d  %(message)s"
        },
        "timestamped": {"format": "%(asctime)s %(levelname)s %(name)s  %(message)s"},
        "simple": {"format": "%(levelname)s  %(message)s"},
        "performance": {
            "format": "%(asctime)s %(process)d | %(thread)d | %(message)s",
        },
    },
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"},
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "timestamped",
        },
        "django": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGGING_DIR, "django.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 10,  # 10 MB
            "backupCount": 10,
        },
        "project": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGGING_DIR, "openpersonen.log"),
            "formatter": "verbose",
            "maxBytes": 1024 * 1024 * 10,  # 10 MB
            "backupCount": 10,
        },
        "performance": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGGING_DIR, "performance.log"),
            "formatter": "performance",
            "maxBytes": 1024 * 1024 * 10,  # 10 MB
            "backupCount": 10,
        },
    },
    "loggers": {
        "openpersonen": {
            "handlers": ["project"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["django"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.template": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    },
}

#
# Additional Django settings
#

TEST_RUNNER = "openpersonen.api.tests.runner.DiscoverRunner"

# Custom user model
AUTH_USER_MODEL = "accounts.User"

# Allow logging in with both username+password and email+password
AUTHENTICATION_BACKENDS = [
    "axes.backends.AxesBackend",
    "openpersonen.accounts.backends.UserModelEmailBackend",
    "django.contrib.auth.backends.ModelBackend",
]

#
# Custom settings
#
PROJECT_NAME = "openpersonen"
ENVIRONMENT = None
SHOW_ALERT = True

#
# Library settings
#


# Django-Admin-Index
ADMIN_INDEX_SHOW_REMAINING_APPS = True
ADMIN_INDEX_AUTO_CREATE_APP_GROUP = True

# Django-Axes (4.0+)
#
# The number of login attempts allowed before a record is created for the
# failed logins. Default: 3
AXES_FAILURE_LIMIT = 10
# If set, defines a period of inactivity after which old failed login attempts
# will be forgotten. Can be set to a python timedelta object or an integer. If
# an integer, will be interpreted as a number of hours. Default: None
AXES_COOLOFF_TIME = 1
# If True only locks based on user id and never locks by IP if attempts limit
# exceed, otherwise utilize the existing IP and user locking logic Default:
# False
AXES_ONLY_USER_FAILURES = True
# If set, specifies a template to render when a user is locked out. Template
# receives cooloff_time and failure_limit as context variables. Default: None
AXES_LOCKOUT_TEMPLATE = "account_blocked.html"
AXES_USE_USER_AGENT = True  # Default: False
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True  # Default: False

# The default meta precedence order
IPWARE_META_PRECEDENCE_ORDER = (
    "HTTP_X_FORWARDED_FOR",
    "X_FORWARDED_FOR",  # <client>, <proxy1>, <proxy2>
    "HTTP_CLIENT_IP",
    "HTTP_X_REAL_IP",
    "HTTP_X_FORWARDED",
    "HTTP_X_CLUSTER_CLIENT_IP",
    "HTTP_FORWARDED_FOR",
    "HTTP_FORWARDED",
    "HTTP_VIA",
    "REMOTE_ADDR",
)

# Django-Hijack
HIJACK_LOGIN_REDIRECT_URL = "/"
HIJACK_LOGOUT_REDIRECT_URL = reverse_lazy("admin:accounts_user_changelist")
# The Admin mixin is used because we use a custom User-model.
HIJACK_REGISTER_ADMIN = False
# This is a CSRF-security risk.
# See: http://django-hijack.readthedocs.io/en/latest/configuration/#allowing-get-method-for-hijack-views
HIJACK_ALLOW_GET_REQUESTS = True

# Sentry SDK
SENTRY_DSN = os.getenv("SENTRY_DSN")

SENTRY_SDK_INTEGRATIONS = [
    django.DjangoIntegration(),
    redis.RedisIntegration(),
]
if celery is not None:
    SENTRY_SDK_INTEGRATIONS.append(celery.CeleryIntegration())

if SENTRY_DSN:
    import sentry_sdk

    SENTRY_CONFIG = {
        "dsn": SENTRY_DSN,
        "release": os.getenv("VERSION_TAG", "VERSION_TAG not set"),
    }

    sentry_sdk.init(
        **SENTRY_CONFIG, integrations=SENTRY_SDK_INTEGRATIONS, send_default_pii=True
    )

# Elastic APM

ELASTIC_APM = {
    "SERVICE_NAME": "openpersonen",
    "SECRET_TOKEN": os.getenv("ELASTIC_APM_SECRET_TOKEN", "default"),
    "SERVER_URL": os.getenv("ELASTIC_APM_SERVER_URL", "http://example.com"),
}


# Swagger Settings
SWAGGER_SETTINGS = BASE_SWAGGER_SETTINGS.copy()
SWAGGER_SETTINGS.update(
    {
        "DEFAULT_INFO": "openpersonen.api.schema.info",
    }
)

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_RENDERER_CLASSES": ("djangorestframework_hal.renderers.HalJSONRenderer",),
    "DEFAULT_PARSER_CLASSES": ("djangorestframework_hal.parsers.HalJSONParser",),
}

# Based on STUF-BG date formats
OPENPERSONEN_YEAR_START = 0
OPENPERSONEN_YEAR_END = 4
OPENPERSONEN_MONTH_START = 4
OPENPERSONEN_MONTH_END = 6
OPENPERSONEN_DAY_START = 6
OPENPERSONEN_DAY_END = 8

OPENPERSONEN_USE_LOCAL_DATABASE = os.getenv("OPENPERSONEN_USE_LOCAL_DATABASE") == "True"
OPENPERSONEN_USE_AUTHENTICATION = not OPENPERSONEN_USE_LOCAL_DATABASE

if os.getenv("OPENPERSONEN_USE_AUTHENTICATION"):
    OPENPERSONEN_USE_AUTHENTICATION = (
        os.getenv("OPENPERSONEN_USE_AUTHENTICATION") == "True"
    )
