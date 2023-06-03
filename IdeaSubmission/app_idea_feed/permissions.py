from rest_framework import permissions


class UpdateOwnIdeaFeed(permissions.BasePermission):
    """Permission class to check that we are updating our own Idea Feed only"""

    def has_object_permission(self, request, view, obj):
        """Check if admin user or a user is trying to update its own idea feed"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.user_profile.id == request.user.id) or (request.user.is_admin == True)