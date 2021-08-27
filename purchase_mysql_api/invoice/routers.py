from rest_framework import routers
from invoice.viewsets import InvoiceViewset

# Register your viewsets here.

# URL pattern: ^basename$ Name: 'basename-list'
# URL pattern: ^basename/{pk}$ Name: 'basename-detail'

router = routers.DefaultRouter(trailing_slash=False)
router.register('invoice', InvoiceViewset, basename='invoice')

urlpatterns=router.urls
