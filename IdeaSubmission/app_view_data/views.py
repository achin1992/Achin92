from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app_view_data import permissions
from app_view_data import serializers
from app_user_actions import models
from app_idea_feed.models import IdeaFeedItem


class ViewLikedIdeasViewSet(viewsets.ModelViewSet):
    """Handles liking an idea"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ViewLikedIdeasSerializer
    permission_classes = (permissions.ViewLikedIdeasOnly, IsAuthenticated,)
    queryset = models.UserLikedIdeas.objects.select_related('idea_feed')

    def list(self, request, *args, **kwargs):
        """Define GET Method"""
        user_id = request.query_params.get('user_id', '')
        if user_id == '':
            user_id = request.user.id
        queryset = models.UserLikedIdeas.objects.filter(user_profile_id=user_id).select_related('idea_feed')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        """POST Method not allowed"""
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        """PUT Method not allowed"""
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        """PATCH Method not allowed"""
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        """DELETE Method not allowed"""
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ViewFavouriteIdeasViewSet(viewsets.ModelViewSet):
    """Handles liking an idea"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ViewLikedIdeasSerializer
    permission_classes = (permissions.ViewFavouriteIdeasOnly, IsAuthenticated,)
    queryset = models.UserFavouriteIdeas.objects.select_related('idea_feed')

    def list(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id', '')
        if user_id == '':
            user_id = request.user.id
        queryset = models.UserFavouriteIdeas.objects.filter(user_profile_id=user_id).select_related('idea_feed')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ViewIdeasFeedViewSet(viewsets.ModelViewSet):
    """Handles liking an idea"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ViewIdeasFeed
    permission_classes = (IsAuthenticated, permissions.ViewIdeasFeedOnly)
    queryset = IdeaFeedItem.objects.order_by('created_on', 'name')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'tags', 'stage', 'user_profile__name')


class ViewIdeasCompleteFeedViewSet(viewsets.ModelViewSet):
    """Handles getting complete idea feed with likes and comments"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ViewIdeasCompleteFeed
    permission_classes = (IsAuthenticated, permissions.ViewIdeasFeedOnly)
    queryset = IdeaFeedItem.objects.order_by('created_on', 'name')
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'tags', 'stage', 'user_profile__name')