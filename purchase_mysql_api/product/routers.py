from rest_framework import routers
from product.viewsets import ProductCategoryViewset, ProductViewset

# Register your viewsets here.

# URL pattern: ^basename$ Name: 'basename-list'
# URL pattern: ^basename/{pk}$ Name: 'basename-detail'

router = routers.DefaultRouter(trailing_slash=False)
router.register('product-category', ProductCategoryViewset, basename='product-category')
router.register('product', ProductViewset, basename='product')

urlpatterns=router.urls
