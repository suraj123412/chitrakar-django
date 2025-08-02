# order/models.py

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15) 
    portrait_type = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    image = models.ImageField(upload_to='orders/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.portrait_type} ({self.size})"
