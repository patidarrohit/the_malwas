from django.contrib import admin
from .models import Order
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_date', 'item_name', 'quantity', 'price', 'total', 'order_status', 'description', 'delivery_date', 'delivery_type', 'customer_name', 'customer_phone', 'customer_email', 'customer_address']
    #raw_id_fields = ['order_date']
