from django.contrib import admin
from product.models import Product, ProductCategory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)