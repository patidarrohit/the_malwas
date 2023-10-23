from django.forms import ModelForm, DateTimeInput
from .models import Order

delivery_choice = (("PICKUP", "Pickup"), ("HOMEDELIVERY", "Home Delivery"), ("MEETSOMEWHERE", "Meed Somewhere"))
item_choice = (("CAKE", "Cake"), ("SWEETS", "Sweets"), ("SNACKS", "Snacks"))
status_choice = (("New Order", "New Order"), ("INPROGRESS", "In Progress"), ("ADVANCEMADE", "Advance Made"), ("ORDERREADY", "Order Ready"), ("PAYMENTINFULL", "Payment In Full"), ("DELIVERED", "Delivered"))


class DateTimeInpt(DateTimeInput):
    input_type = 'datetime-local'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['item_name', 'quantity', 'price', 'total', 'order_status', 'description', 'delivery_date', 'delivery_type', 'customer_name', 'customer_phone', 'customer_email', 'customer_address']
    # order_date = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
    # order_status = forms.ChoiceField(choices=status_choice)
    # item_name = forms.CharField(max_length=100)
    # description = forms.CharField(max_length=500)
    # quantity = forms.CharField()
    # price = forms.DecimalField(min_value=0.00, decimal_places=2)
    # total = forms.DecimalField(decimal_places=2)
    # delivery_date = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}))
    # delivery_type = forms.ChoiceField(choices=delivery_choice)
    # customer_name = forms.CharField(max_length=50)
    # customer_phone = forms.CharField(max_length=15)
    # customer_email = forms.EmailField()
    # customer_address = forms.CharField(max_length=50)
        widgets = {
            'delivery_date': DateTimeInpt,
        }