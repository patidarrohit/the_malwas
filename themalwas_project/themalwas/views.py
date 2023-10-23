from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from .forms import OrderForm
from .models import Order


# Create your views here.
def home(request):
    return render(request, 'themalwas/home.html', {'section': ''})


#@staff_member_required(login_url=reverse_lazy('login'))
@user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('login'))
def order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            print(order_form.cleaned_data)
            order_form.save()
            orders_lst = Order.objects.all()
            return render(request, 'themalwas/orders_list.html', {'orders_list': orders_lst})
    else:
        order_form = OrderForm()
    return render(request, 'themalwas/order.html', {'order_form': order_form})


@user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('login'))
def orders_list(request):
    orders_lst = Order.objects.all()
    return render(request, 'themalwas/orders_list.html', {'orders_list': orders_lst})


