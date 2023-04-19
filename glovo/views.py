from django.shortcuts import render

from .models import Order


def get_order(request):
    orders = Order.objects.all()
    return render(request, 'get_order.html', {'orders': orders})