from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)  # Example field: name of the destination
    description = models.TextField()  # Example field: description of the destination
    image = models.ImageField(upload_to='destination_images/')  # Example field: image of the destination
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation date
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update date