from django_filters import rest_framework as filters
from invoice.models import Invoice

# Create your filters here.

class InvoiceFilterset(filters.FilterSet):
    class Meta:
        model = Invoice
        fields = {
            'created_by__id': ['exact'],
            'created_at': ['year__exact', 'year__gte', 'month__exact', 'day__exact'],
            'product__id': ['exact'],
            'product__category__name': ['exact'],
            'amount': ['gte', 'lte'],
        }