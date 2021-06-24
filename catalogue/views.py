"""View based to catalogue."""

# Django libraries
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Models
from catalogue.models import CategoryModel
from catalogue.models import ItemModel


# VBF
def index(request):
    items = ItemModel.objects.filter(stock=True).order_by('name')  # Lista todos los productos disponibles
    categories = CategoryModel.objects.order_by('name')  # Lista todas las categorías de bd ordenadas asc por nombre
    param = request.GET.get("search", None)
    param_category = request.GET.get("search-category", None)  # Category.id
    if param or param_category:
        # Q(question__startswith='Who') | Q(question__startswith='What')
        items = items.filter(
            Q(name__icontains=param)
            | Q(category__name__icontains=param)
            | Q(category__pk__exact=int(param_category))
        )
    return render(request, 'catalogue/index.html', {'categories': categories, "items": items})


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


def item_detail(request, id: int):
    try:
        item = ItemModel.objects.get(id=id)
    except ItemModel.DoesNotExist:
        item = None
    return render(request, "catalogue/item_detail.html", {"item": item})
