from django.contrib import admin
from customer.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'location')

admin.site.register(Customer, CustomerAdmin)