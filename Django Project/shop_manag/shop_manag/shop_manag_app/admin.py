from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order_Product)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(Delivery_Address)

