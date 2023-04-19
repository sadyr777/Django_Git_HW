from django.shortcuts import render

from .models import Courier, Order


def get_courier(request):
    couriers = Courier.objects.all()
    return render(request, 'get_courier.html', {'couriers': couriers})


def get_order(request):
    orders = Order.objects.all()
    return render(request, 'get_order.html', {'orders': orders})
