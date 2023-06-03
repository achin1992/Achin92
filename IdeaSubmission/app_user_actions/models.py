from django.db import models
from django.conf import settings

from app_idea_feed.models import IdeaFeedItem


class UserLikedIdeas(models.Model):
    """To store ideas liked by a user"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='liked_user',
        on_delete=models.CASCADE
    )
    idea_feed = models.ForeignKey(
        IdeaFeedItem,
        related_name='liked_idea',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_profile', 'idea_feed')


class UserFavouriteIdeas(models.Model):
    """To store user's favourite ideas"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='favourite_user',
        on_delete=models.CASCADE
    )
    idea_feed = models.ForeignKey(
        IdeaFeedItem,
        related_name='favourite_user',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_profile', 'idea_feed')


class UserCommentIdeas(models.Model):
    """To store ideas liked by a user"""

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='comments_user',
        on_delete=models.CASCADE
    )
    idea_feed = models.ForeignKey(
        IdeaFeedItem,
        related_name='comments_idea',
        on_delete=models.CASCADE
    )
    comment = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)