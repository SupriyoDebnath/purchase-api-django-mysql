from rest_framework import viewsets
from product.serializers import ProductSerializer, ProductCategorySerializer
from product.models import Product, ProductCategory
from product.filters import ProductFilterset

# Create your viewsets here.

class ProductCategoryViewset(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all().order_by('-created_at')
    http_method_names = ['get', 'head']


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_deleted=False).order_by('-created_at')
    filter_class = ProductFilterset
    http_method_names = ['get', 'head']
