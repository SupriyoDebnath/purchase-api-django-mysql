from rest_framework import serializers
from invoice.models import Invoice

# Create your serializers here.

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'