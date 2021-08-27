from rest_framework import routers
from customer.viewsets import CustomerViewset

# Register your viewsets here.

# URL pattern: ^basename$ Name: 'basename-list'
# URL pattern: ^basename/{pk}$ Name: 'basename-detail'

router = routers.DefaultRouter(trailing_slash=False)
router.register('customer', CustomerViewset, basename='customer')

urlpatterns=router.urls
