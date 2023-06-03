from rest_framework import serializers

from app_user_actions import models
from app_idea_feed.serializers import IdeaFeedItemSerializer
from user_profiles_api.serializers import UserProfileSerializer


class UserLikedIdeasSerializer(serializers.ModelSerializer):
    """Serializes user liked ideas"""

    class Meta:
        model = models.UserLikedIdeas
        fields = ('id', 'user_profile', 'idea_feed')
        extra_kwargs = {'user_profile': {'read_only': True}}


class UserFavouriteIdeasSerializer(serializers.ModelSerializer):
    """Serializes user favourite ideas"""

    class Meta:
        model = models.UserFavouriteIdeas
        fields = ('id', 'user_profile', 'idea_feed')
        extra_kwargs = {'user_profile': {'read_only': True}}


class UserCommentIdeasSerializer(serializers.ModelSerializer):
    """Serializes user's comment on ideas"""

    class Meta:
        model = models.UserCommentIdeas
        fields = ('id', 'user_profile', 'idea_feed', 'comment')
        extra_kwargs = {'user_profile': {'read_only': True}}


class IdeaLikedByUsersSerializer(serializers.ModelSerializer):
    """Serializes ideas liked by user with their details"""

    user_profile = UserProfileSerializer()

    class Meta:
        model = models.UserLikedIdeas
        fields = ('id', 'user_profile', 'idea_feed')
        extra_kwargs = {'user_profile': {'read_only': True}}


class IdeaCommentByUsersSerializer(serializers.ModelSerializer):
    """Serializes ideas liked by user with their details"""

    user_profile = UserProfileSerializer()

    class Meta:
        model = models.UserCommentIdeas
        fields = ('id', 'user_profile', 'idea_feed', 'comment')
        extra_kwargs = {'user_profile': {'read_only': True}}