from .dev import *  # noqa isort:skip

DATABASES['stufbg'] = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.getenv("STUF_BG_DB_NAME", "stufbg"),
    "USER": os.getenv("STUF_BG_DB_USER", "stufbg"),
    "PASSWORD": os.getenv("STUF_BG_DB_PASSWORD", "stufbg"),
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", 5432),
}

USE_STUF_BG_DATA = True
