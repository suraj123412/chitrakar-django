from django.db import models

# Create your models here.
class FeaturedPortrait(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portraits/')
    size = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=100 , default="Anonymous")
    comment = models.TextField(default="No comment")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.comment[:30]}"
    

    
    
