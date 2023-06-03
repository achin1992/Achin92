from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app_user_actions import permissions
from app_user_actions import serializers
from app_user_actions import models


class UserLikedIdeasViewSet(viewsets.ModelViewSet):
    """Handles liking an idea"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserLikedIdeasSerializer
    permission_classes = (permissions.LikeWithCurrentUser, IsAuthenticated,)
    queryset = models.UserLikedIdeas.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserFavouriteIdeasViewSet(viewsets.ModelViewSet):
    """Handles marking idea as favourite"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserFavouriteIdeasSerializer
    permission_classes = (permissions.MarkFavouriteWithCurrentUser, IsAuthenticated,)
    queryset = models.UserFavouriteIdeas.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserCommentIdeasViewSet(viewsets.ModelViewSet):
    """Handles commenting on an idea"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserCommentIdeasSerializer
    permission_classes = (permissions.CommentWithCurrentUser, IsAuthenticated,)
    queryset = models.UserCommentIdeas.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)