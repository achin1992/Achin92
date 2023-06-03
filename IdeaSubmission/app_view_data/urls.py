from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_view_data import views

router = DefaultRouter()
router.register('like', views.ViewLikedIdeasViewSet)
router.register('favourite', views.ViewFavouriteIdeasViewSet)
router.register('ideas_only', views.ViewIdeasFeedViewSet)
router.register('ideas', views.ViewIdeasCompleteFeedViewSet)

urlpatterns = [
    path('', include(router.urls))
]