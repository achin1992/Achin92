from rest_framework import permissions


class LikeWithCurrentUser(permissions.BasePermission):
    """Permission class to check that only logged in user likes an idea"""

    def has_object_permission(self, request, view, obj):
        """Check if logged in user is trying to like an idea"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return (request.method not in ('PATCH', 'PUT')) and (obj.user_profile.id == request.user.id)


class MarkFavouriteWithCurrentUser(permissions.BasePermission):
    """Permission class to check that only logged in marks idea as favourite"""

    def has_object_permission(self, request, view, obj):
        """Check if logged in user is trying to mark idea as favourite"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return (request.method not in ('PATCH', 'PUT')) and (obj.user_profile.id == request.user.id)


class CommentWithCurrentUser(permissions.BasePermission):
    """Permission class to check that only logged in user can comment on an idea"""

    def has_object_permission(self, request, view, obj):
        """Check if logged in user is trying to comment on an idea"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return (request.method not in ('PATCH', 'PUT')) and (obj.user_profile.id == request.user.id)
