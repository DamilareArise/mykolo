from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="image-thumbnail/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    