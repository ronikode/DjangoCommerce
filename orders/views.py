from django.contrib import messages
from django.shortcuts import render

from django.db import transaction
from orders.forms import OrderCreateForm


@transaction.atomic
def order_create(request):
    form = OrderCreateForm()
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                order = form.save()  # Basado en un model Form de OrderModel puedo guardar en base datos.
                messages.success(request, "Orden creada exitosamente.")
    return render(request, "orders/order_create.html", {'form': form})
