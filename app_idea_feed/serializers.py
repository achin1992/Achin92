from rest_framework import serializers
from app_idea_feed import models


class IdeaFeedItemSerializer(serializers.ModelSerializer):
    """Serializes idea feed items"""

    class Meta:
        model = models.IdeaFeedItem
        fields = ('id', 'user_profile', 'name', 'description', 'theme', 'department',
                  'rag_status', 'tags', 'stage', 'contributor', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True},
            'stage': {'read_only': True}
        }