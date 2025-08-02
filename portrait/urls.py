
from rest_framework.routers import DefaultRouter
from .views import FeaturedPortraitViewSet , CommentViewSet 

router = DefaultRouter()
router.register(r'portrait/featured', FeaturedPortraitViewSet, basename='featured'),
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns =(router.urls)