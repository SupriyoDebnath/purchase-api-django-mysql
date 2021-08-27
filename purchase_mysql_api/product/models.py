from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='pc_created_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_category' 
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='p_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True, related_name='p_modified_by')
    modified_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.RESTRICT, related_name='p_category')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'product' 
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
