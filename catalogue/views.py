"""View based to catalogue."""

# Django libraries
from django.shortcuts import render


# VBF
def catalogue(request):
    # TODO: Logic
    title: str = "Empresa online"
    return render(request, 'catalogue/index.html', {"title_b": title})

# VBC
