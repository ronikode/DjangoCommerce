"""Forms django"""

from django import forms

from customers.models import CustomerModel


class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerModel
        fields = ("full_name", "dni")

    # TODO: Validations
