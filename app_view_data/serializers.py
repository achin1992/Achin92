from rest_framework import serializers

from app_idea_feed.serializers import IdeaFeedItemSerializer
from user_profiles_api.serializers import UserProfileSerializer
from app_user_actions.serializers import UserLikedIdeasSerializer, \
    IdeaLikedByUsersSerializer, IdeaCommentByUsersSerializer

from app_user_actions.models import UserLikedIdeas, UserFavouriteIdeas
from app_idea_feed.models import IdeaFeedItem


class ViewLikedIdeasSerializer(serializers.ModelSerializer):
    """Serializes user liked ideas"""

    user_profile = UserProfileSerializer()
    idea_feed = IdeaFeedItemSerializer()

    class Meta:
        model = UserLikedIdeas
        fields = ('id', 'user_profile', 'idea_feed')
        extra_kwargs = {'user_profile': {'read_only': True}}


class ViewFavouriteIdeasSerializer(serializers.ModelSerializer):
    """Serializes user favourite ideas"""

    user_profile = UserProfileSerializer()
    idea_feed = IdeaFeedItemSerializer()

    class Meta:
        model = UserFavouriteIdeas
        fields = ('id', 'user_profile', 'idea_feed')
        extra_kwargs = {'user_profile': {'read_only': True}}


class ViewIdeasFeed(serializers.ModelSerializer):
    """Serializes ideas feed for view"""

    user_profile = UserProfileSerializer()

    class Meta:
        model = IdeaFeedItem
        fields = ('id', 'user_profile', 'name', 'description', 'theme', 'department',
                  'rag_status', 'tags', 'stage', 'contributor', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


class ViewIdeasCompleteFeed(serializers.ModelSerializer):
    """Serializes complete ideas feed for view with likes and comments"""

    user_profile = UserProfileSerializer()
    liked_idea = IdeaLikedByUsersSerializer(many=True)
    comments_idea = IdeaCommentByUsersSerializer(many=True)

    class Meta:
        model = IdeaFeedItem
        fields = ('id', 'user_profile', 'liked_idea', 'comments_idea', 'name', 'description',
                  'theme', 'department', 'rag_status', 'tags', 'stage', 'contributor', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}