from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    size = models.CharField(max_length=50, help_text='e.g. A3, A4, Custom')
    category = models.CharField(max_length=50, help_text='e.g. Portrait, Sketch, Color')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title