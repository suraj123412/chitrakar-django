# order/serializers.py

from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # username return होईल

    class Meta:
        model = Order
        fields = '__all__'  
