from django.contrib import admin

from user_profiles_api import models


admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
