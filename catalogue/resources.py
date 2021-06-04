from import_export import resources
from import_export.fields import Field

from catalogue.models import ItemModel


class ItemResource(resources.ModelResource):
    sku = Field(attribute="sku", column_name="CODIGO")

    class Meta:
        model = ItemModel

    def after_export(self, queryset, data, *args, **kwargs):
        pass