from django.shortcuts import render

from .models import Courier


def get_courier(request):
    couriers = Courier.objects.all()
    return render(request, 'get_courier.html', {'couriers': couriers})
