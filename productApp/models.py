from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Products(models.Model):
    STATUS_CHOICES = [
        ("IN_STOCK", "In Stock"),
        ("OUT_OF_STOCK", "Out Of Stock")
    ]
    
    
    
    title = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="image-thumbnail/", null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="OUT_OF_STOCK")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class ProductSpec(models.Model):
    field_name = models.CharField(max_length=100, null=True, blank=True)
    field_value = models.CharField(max_length=100, null=True, blank=True)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, related_name="specs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.title}-{self.field_name}"
    
