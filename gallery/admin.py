from django.contrib import admin
from .models import GalleryImage


# Register your models here.
@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image' , 'category', 'image', 'created_at')
    search_fields = ('title', 'category', 'image')
    list_filter = ('category', 'image', 'created_at')