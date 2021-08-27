from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils.timezone import get_current_timezone
from customer.serializers import CustomerSerializer
from customer.models import Customer
from customer.filters import CustomerFilterset

# Create your viewsets here.

class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter(is_deleted=False).order_by('-created_at')
    filter_class = CustomerFilterset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {
            'is_deleted': True,
            'modified_at': datetime.now(tz=get_current_timezone()), 
            'modified_by': instance.id
        }
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)