from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
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
@login_required(login_url='/security/login/')
def customer_detail(request, identifier: int):
    try:
        customer = CustomerModel.objects.get(id=identifier)
    except CustomerModel.DoesNotExist:
        customer = None
    return render(request, "customers/detail.html", {"customer": customer})


# CREAR
@login_required(login_url='/security/login/')
def customers_create(request):
    form = BasicCustomerForm()
    if request.method == "POST":
        form = BasicCustomerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data  # -> dict {"full_name": <>, "dni": <>}
            # customer = CustomerModel()
            # customer.full_name = data.get('full_name')
            # customer.dni = data.get('dni')
            # customer.save()
            CustomerModel.objects.create(
                full_name=data.get("full_name"), dni=data.get("dni"),
                created_by=request.user
            )
            messages.success(request, "Cliente registrado exitosamente.")
            return redirect(reverse_lazy("customers:customers_list"))
        else:
            messages.error(request, "Error al crear un cliente")
    return render(request, 'customers/create.html', {"form": form})


# ACTUALIZAR
@login_required(login_url='/security/login/')
def customers_edit(request, identifier: int):
    # 1. Obtener el registro a editar.
    try:
        customer = CustomerModel.objects.get(id=identifier)
    except CustomerModel.DoesNotExist:
        customer = None

    form = BasicCustomerForm()
    if customer is not None:
        form = BasicCustomerForm(initial={"full_name": customer.full_name, "dni": customer.dni})
        if request.method == "POST":
            form = BasicCustomerForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                customer.full_name = data.get("full_name")
                customer.dni = data.get("dni")

                customer.modified_at = datetime.now()
                customer.modified_by = request.user
                customer.save()
                messages.success(request, "Cliente modificado exitosamente.")
                return redirect(reverse_lazy("customers:customers_list"))
            else:
                messages.error(request, "Error al editar un cliente")
    return render(request, "customers/update.html", {"form": form})


# BORRAR
@login_required(login_url='/security/login/')
def customers_delete(request, id: int):
    customer = get_object_or_404(CustomerModel, id=id, status=True)

    # CRITERIOS PARA BORRAR
    customer.deleted_at = datetime.now()
    customer.status = False
    customer.save()
    messages.success(request, "Cliente ha sido eliminado exitosamente.")
    return redirect(reverse_lazy("customers:customers_list"))
