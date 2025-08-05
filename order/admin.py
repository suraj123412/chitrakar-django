from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'portrait_type','image','size', 'user', 'created_at')
    search_fields = ('name', 'portrait_type', 'size', 'user__username')
    list_filter = ('portrait_type', 'size', 'created_at')
