from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.db.models import F
from django.utils.timezone import get_current_timezone
from django.db import transaction
from invoice.serializers import InvoiceSerializer
from invoice.models import Invoice
from invoice.filters import InvoiceFilterset
from product.models import Product
from purchase_mysql_api.settings import API_USER_ID

# Create your viewsets here.

class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all().order_by('-created_at')
    filter_class = InvoiceFilterset
    http_method_names = ['get', 'head', 'post']

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        product_list = request.data['product']
        product_quantity_list = request.data['product_quantity']
        for i in range(len(product_list)):
            Product.objects.filter(id=product_list[i]).\
                update(quantity=F('quantity')-product_quantity_list[i], 
                        modified_by=API_USER_ID,
                        modified_at=datetime.now(tz=get_current_timezone()))

        headers = {}
        try:
            headers = {'Location': str(serializer.data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            pass

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
