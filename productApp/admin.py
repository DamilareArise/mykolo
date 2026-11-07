from django.contrib import admin
from .models import Products, ProductSpec, Category

# Register your models here.

admin.site.register([Products, ProductSpec, Category])