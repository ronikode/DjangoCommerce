"""View based to catalogue."""

# Django libraries
from django.shortcuts import render, get_object_or_404

# Models
from catalogue.models import CategoryModel
from catalogue.models import ItemModel


# VBF
def index(request):
    # TODO: Logic
    title: str = "Empresa online"
    categories = CategoryModel.objects.order_by('name')  # Lista todas las categorías de bd ordenadas asc por nombre
    items = ItemModel.objects.filter(stock=True).order_by('name')  # Lista todos los productos disponibles
    return render(request, 'catalogue/index.html', {"title_b": title, 'categories': categories, "items": items})


def category_items(request, category_slug=None):
    # Envia excepcion si no lo encuentra o una instancia objeto -> categoría
    category = get_object_or_404(CategoryModel, code=category_slug)
    filtered_items = ItemModel.objects.filter(category=category)  # Lista filtrada por categoría.
    if filtered_items.exists():
        message = "Existe elementos"
        flag = True
    else:
        flag = False
        message = "No existe intems asociados a esa categoría"
    return render(request, '', {"filtered_items": filtered_items, "flag": flag, "message": message})
