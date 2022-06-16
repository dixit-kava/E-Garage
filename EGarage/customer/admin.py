from django.contrib import admin
from customer.models import contact, Customer, Order, Service


admin.site.register(contact)
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Order)


