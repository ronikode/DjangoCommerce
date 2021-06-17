from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from customers.forms import BasicCustomerForm
# Import customer model
from customers.models import CustomerModel


# LISTAR


def customers_list(request):
    customers = CustomerModel.objects.filter(status=True).order_by("full_name")
    return render(request, "customers/list.html", {"customers": customers})


# OBTENER

# CREAR
def customers_create(request):
    form = BasicCustomerForm()
    if request.method == "POST":
        form = BasicCustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # -> dict {"full_name": <>, "dni": <>}
            customer = CustomerModel()
            customer.full_name = data.get('full_name')
            customer.dni = data.get('dni')
            customer.save()
            messages.success(request, "Cliente registrado exitosamente.")
            return redirect(reverse_lazy("customers:customers_list"))
        else:
            messages.error(request, "Error al crear un cliente")
    return render(request, 'customers/create.html', {"form": form})

# ACTUALIZAR

# BORRAR
