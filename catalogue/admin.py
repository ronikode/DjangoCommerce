from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from catalogue.models import ItemModel


@admin.register(ItemModel)
class ItemModelAdmin(ImportExportModelAdmin):
    search_fields = ("name", "sku")
    list_display = ("name", "pvp", "description")
    list_filter = ("pvp", "stock")