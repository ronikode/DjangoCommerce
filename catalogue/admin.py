import admin_thumbnails
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from catalogue.models import ItemModel, CategoryModel


@admin.register(ItemModel)
@admin_thumbnails.thumbnail('photo', 'Thumbnail')
class ItemModelAdmin(ImportExportModelAdmin):
    search_fields = ("name", "sku")
    list_display = ("name", "photo_thumbnail", "category", "pvp", "description")
    list_filter = ("category", "pvp", "stock")
    raw_id_fields = ("category",)
    fields = ("name", "sku", "pvp", "category", "photo", "stock", "description")


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "code")

