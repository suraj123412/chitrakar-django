from .serializers import FeaturedPortraitSerializer ,CommentSerializer 
from .models import FeaturedPortrait , Comment 
from rest_framework import viewsets 
from rest_framework.permissions import AllowAny


# Create your views here.
class FeaturedPortraitViewSet(viewsets.ModelViewSet):
    queryset = FeaturedPortrait.objects.all()
    serializer_class = FeaturedPortraitSerializer
    permission_classes = [AllowAny]  
    
class CommentViewSet(viewsets.ModelViewSet):  
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]  
    
