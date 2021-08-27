from django_filters import rest_framework as filters
from customer.models import Customer

# Create your filters here.

class CustomerFilterset(filters.FilterSet):
    class Meta:
        model = Customer
        fields = {
            'fullname': ['icontains'],
            'created_at': ['year__exact', 'year__gte'],
            'email': ['startswith'],
            'location': ['exact'],
        }