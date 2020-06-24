from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app_idea_feed import permissions
from app_idea_feed import serializers
from app_idea_feed import models


class IdeaFeedItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating idea feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.IdeaFeedItemSerializer
    permission_classes = (permissions.UpdateOwnIdeaFeed, IsAuthenticated,)
    queryset = models.IdeaFeedItem.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
