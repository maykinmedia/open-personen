from django.conf import settings

from rest_framework.permissions import IsAuthenticated as _IsAuthenticated


class IsAuthenticated(_IsAuthenticated):
    def has_permission(self, request, view):
        if settings.USE_AUTHENTICATION:
            return super().has_permission(request, view)
        else:
            return True
