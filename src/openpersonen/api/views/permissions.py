from django.conf import settings

from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if settings.USE_AUTHENTICATION:
            return bool(request.user and request.user.is_authenticated)
        else:
            return True
