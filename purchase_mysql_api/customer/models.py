from django.db import models
from django.utils.text import slugify

# Create your models here.

class Customer(models.Model):
    LOCATION_CHOICES = [
        ('IND', 'India -- Default'),
        ('SG', 'Singapore')
    ]

    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='IND')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'customer' 
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        self.slug = slugify(self.fullname)
        super(Customer, self).save(*args, **kwargs)
