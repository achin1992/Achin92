from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_idea_feed import views

router = DefaultRouter()
router.register('feed', views.IdeaFeedItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]