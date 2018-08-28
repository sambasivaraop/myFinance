"""Define set of permissions."""
import logging

from rest_framework import permissions

LOGGER = logging.getLogger(__name__)


class UserViewSetPermission(permissions.BasePermission):
    """Custom permission class for User view set."""

    def has_permission(self, request, view):
        user = request.user
        if user.user_type == 'admin':
            return True
        LOGGER.debug("User type is not admin, returning false")
        return False

    def has_object_permission(self, request, view, obj):
        # Instance must have an attribute named `email`.
        if request.user.user_type == "admin":
            return True
        return obj.email == request.user.email
