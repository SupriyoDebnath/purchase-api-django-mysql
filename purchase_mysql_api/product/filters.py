from django_filters import rest_framework as filters
from product.models import Product

# Create your filters here.

class ProductFilterset(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'created_at': ['year__exact', 'year__gte'],
            'category__id': ['exact'],
            'category__name': ['exact'],
            'price': ['gte', 'lte'],
        }