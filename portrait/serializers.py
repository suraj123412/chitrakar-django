from rest_framework import serializers 
from .models import FeaturedPortrait, Comment 

class FeaturedPortraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedPortrait
        fields = '__all__'

    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

