from django.db import models
from django.conf import settings


class IdeaFeedItem(models.Model):
    """To store idea submitted by application users"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=400)
    theme = models.CharField(max_length=25, default="Data Science")
    department = models.CharField(max_length=25, default="Finance")
    rag_status = models.CharField(max_length=15, default="Green")
    tags = models.CharField(max_length=150, default="#Innovation")
    stage = models.CharField(max_length=20, default="Idea Initiation")
    contributor = models.CharField(max_length=100, default="MentorA")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the model as string"""
        return self.name