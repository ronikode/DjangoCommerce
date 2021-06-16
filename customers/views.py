from django.shortcuts import render

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
            # TODO:
        else:
            print("Error")
    return render(request, 'customers/create.html', {"form": form})

# ACTUALIZAR

# BORRAR
