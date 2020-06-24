from django.contrib import admin

from app_user_actions import models

admin.site.register(models.UserLikedIdeas)
admin.site.register(models.UserFavouriteIdeas)
admin.site.register(models.UserCommentIdeas)