import os
import warnings

os.environ.setdefault(
    "SECRET_KEY", "%9+dfjw+zd3@q)ehsx(pdwy-ueq0zt=90gb4+&qd^6ytpj@p7#"
)

# uses postgresql by default, see base.py
os.environ.setdefault("DB_NAME", "openpersonen"),
os.environ.setdefault("DB_USER", "openpersonen"),
os.environ.setdefault("DB_PASSWORD", "openpersonen"),

os.environ.setdefault("SENDFILE_BACKEND", "django_sendfile.backends.development"),

from .base import *  # noqa isort:skip

# Feel free to switch dev to sqlite3 for simple projects,
# or override DATABASES in your local.py
# DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

#
# Standard Django settings.
#

DEBUG = True
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ADMINS = ()
MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

LOGGING["loggers"].update(
    {
        "openpersonen": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["django"],
            "level": "DEBUG",
            "propagate": False,
        },
        "performance": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        #
        # See: https://code.djangoproject.com/ticket/30554
        # Autoreload logs excessively, turn it down a bit.
        #
        "django.utils.autoreload": {
            "handlers": ["django"],
            "level": "INFO",
            "propagate": False,
        },
    }
)

#
# Additional Django settings
#

# Disable security measures for development
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False

#
# Custom settings
#
ENVIRONMENT = "development"

#
# Library settings
#

# Django-Admin-Index
ADMIN_INDEX_SHOW_REMAINING_APPS_TO_SUPERUSERS = True

# Elastic APM
ELASTIC_APM["DEBUG"] = True

# Django debug toolbar
INSTALLED_APPS += ["debug_toolbar", "ddt_api_calls"]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
INTERNAL_IPS = ("127.0.0.1",)
DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "ddt_api_calls.panels.APICallsPanel",
]

AXES_BEHIND_REVERSE_PROXY = (
    False  # Default: False (we are typically using Nginx as reverse proxy)
)


AXES_CACHE = "axes_cache"


# THOU SHALT NOT USE NAIVE DATETIMES
warnings.filterwarnings(
    "error",
    r"DateTimeField .* received a naive datetime",
    RuntimeWarning,
    r"django\.db\.models\.fields",
)

# Override settings with local settings.
try:
    from .local import *  # noqa
except ImportError:
    pass
