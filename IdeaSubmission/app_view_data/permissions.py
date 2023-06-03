from rest_framework import permissions


class ViewLikedIdeasOnly(permissions.BasePermission):
    """Class to ensure only GET request is processed to view liked ideas"""

    def has_object_permission(self, request, view, obj):
        """Check if it is a GET request"""
        return self.request.method in permissions.SAFE_METHODS


class ViewFavouriteIdeasOnly(permissions.BasePermission):
    """Class to ensure only GET request is processed to view ideas as favourite"""

    def has_object_permission(self, request, view, obj):
        """Check if it is a GET request"""
        return self.request.method in permissions.SAFE_METHODS


class ViewIdeasFeedOnly(permissions.BasePermission):
    """Class to ensure only GET request is processed to view ideas as favourite"""

    def has_object_permission(self, request, view, obj):
        """Check if it is a GET request"""
        return bool(self.request.method in permissions.SAFE_METHODS and request.user.is_authenticated)