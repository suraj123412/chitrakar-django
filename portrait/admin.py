from django.contrib import admin
from .models import FeaturedPortrait, Comment 

# Register your models here.

    
@admin.register(FeaturedPortrait)
class FeaturedPortraitAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'created_at')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'created_at')
    search_fields = ('name', 'comment')
    list_filter = ('created_at',)