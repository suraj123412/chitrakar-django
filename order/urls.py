# order/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet , OrderDetailView

urlpatterns = [ 
 path('users/', OrderViewSet.as_view(), name='order-list-create'),
  path('users/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]