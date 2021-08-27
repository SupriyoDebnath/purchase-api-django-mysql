import uuid
from django.db import models
from customer.models import Customer
from product.models import Product

# Create your models here.

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100, blank=True, unique=True)
    created_by = models.ForeignKey(Customer, on_delete=models.RESTRICT, related_name='i_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField(Product)
    product_quantity = models.JSONField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    views = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)

    class Meta:
        db_table = 'invoice' 
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.label = uuid.uuid4()
        super(Invoice, self).save(*args, **kwargs)
