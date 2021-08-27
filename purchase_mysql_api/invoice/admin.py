from django.contrib import admin
from invoice.models import Invoice

# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('label', 'get_customer_name', 'amount', 'created_at')
    list_filter = ['created_by__fullname']
    filter_horizontal = ('product',)

    def get_customer_name(self, obj):
        return obj.created_by.fullname
    
    get_customer_name.short_description = 'customer'

admin.site.register(Invoice, InvoiceAdmin)