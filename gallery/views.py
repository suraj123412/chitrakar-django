from rest_framework import viewsets, filters
from .models import GalleryImage
from .serializers import GalleryImageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all().order_by('-created_at')
    serializer_class = GalleryImageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [AllowAny] 
