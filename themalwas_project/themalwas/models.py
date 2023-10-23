from django.db import models

delivery_choice = (("Pickup", "Pickup"), ("Home Delivery", "Home Delivery"), ("Meet Somewhere", "Meet Somewhere"))
# item_choice = (("CAKE", "Cake"), ("SWEETS", "Sweets"), ("SNACKS", "Snacks"))
status_choice = (("New Order", "New Order"), ("In Progress", "In Progress"), ("Advance Made", "Advance Made"), ("Order Ready", "Order Ready"), ("Payment In Full", "Payment In Full"), ("Delivered", "Delivered"))


# Create your models here.
class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    order_status = models.CharField(max_length=50, choices=status_choice)
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_date = models.DateTimeField()
    delivery_type = models.CharField(max_length=20, choices=delivery_choice)
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField(blank=True, null=True)
    customer_address = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


