"""Forms django"""

from django import forms
from django.core.exceptions import ValidationError

from customers.models import CustomerModel


def validation_sri_dni(value):
    # TODO: Aplicar algoritmo de validacion de no. id
    print(value)
    return True


class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ("full_name", "dni")

    # TODO: Validations

    def clean_dni(self):
        dni = self.cleaned_data.get("dni")
        if len(dni) < 10:
            raise ValidationError("Error No. de Identificación incorrecto")
        return dni
