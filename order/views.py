# # order/views.py

# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from .models import Order
# from .serializers import OrderSerializer

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by('-created_at')
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]  

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

# 1. List & Create - /api/order/users/
class OrderViewSet(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 2. Retrieve, Update, Delete - /api/order/users/<int:pk>/
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

