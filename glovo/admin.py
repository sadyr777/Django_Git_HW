from django.contrib import admin
from .models import Order, Courier

admin.site.register(Courier)

admin.site.register(Order)
