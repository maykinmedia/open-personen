"""
WSGI config for openpersonen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import os

from django.core.wsgi import get_wsgi_application

from openpersonen.setup import setup_env

setup_env()

application = get_wsgi_application()
