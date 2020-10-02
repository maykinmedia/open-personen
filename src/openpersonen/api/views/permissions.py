from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from rest_framework.permissions import IsAuthenticated as _IsAuthenticated


class IsAuthenticated(_IsAuthenticated):
    def has_permission(self, request, view):
        if settings.USE_AUTHENTICATION:
            return super().has_permission(request, view)
        else:
            if not settings.USE_STUF_BG_DATABASE:
                raise ImproperlyConfigured(
                    "Must use authentication when not using local database"
                )
            return True
