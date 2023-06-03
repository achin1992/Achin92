from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_user_actions import views

router = DefaultRouter()

router.register('like', views.UserLikedIdeasViewSet)
router.register('comment', views.UserCommentIdeasViewSet)
router.register('favourite', views.UserFavouriteIdeasViewSet)

urlpatterns = [
    path('', include(router.urls))
]