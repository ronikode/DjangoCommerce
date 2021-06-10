from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=150, help_text="Nombre de la categoría")
    description = models.TextField(verbose_name="Descripción", help_text="Descripción de la categoría.", blank=True)
    code = models.CharField(blank=True, verbose_name="Código", max_length=80,
                            help_text="Código referencial de la categoría")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-name']  # order desc
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        db_table = "category"  # -> catalogue__categorymodel


class ItemModel(models.Model):

    # category__items__
    # on_delete=models.CASCADE  -  Si se elimina los intervenientes en la relacion se borra los registros.
    # on_delete=models.PROTECT  -  Si se borra uno de los intervenientes el otro se mantiene.
    # on_delete=models.SET_NULL - Si se borra uno de los intervenientes el otro se setea con null.
    category = models.ForeignKey(
        CategoryModel, on_delete=models.SET_NULL, help_text="Relación con categoría.",
        related_name="items", blank=True, null=True
    )

    sku = models.CharField(verbose_name="Codigo", unique=True, max_length=60)
    name = models.CharField(max_length=200, verbose_name="Nombre", help_text="Nombre del item.")
    pvp = models.DecimalField(max_digits=9, decimal_places=3, verbose_name="Precio",
                              help_text="Precio de venta con IVA")
    photo = models.ImageField(upload_to="item/", verbose_name="Foto", help_text="Foto principal del item.")
    description = models.TextField(verbose_name="Descripción", help_text="Descripción del item.", blank=True,
                                   default="")
    stock = models.BooleanField(default=True, verbose_name="Stock", db_column="existe")

    def __str__(self) -> str:
        return f"[{self.sku}] {self.name}"

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = "item"

    def delete(self, using=None, keep_parents=False):
        pass
        # TODO: Implement soft delete.
