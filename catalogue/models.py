from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class ItemModel(models.Model):
    sku = models.CharField(verbose_name="Codigo", unique=True, max_length=60)
    name = models.CharField(max_length=150, verbose_name="Nombre", help_text="Nombre del item.")
    pvp = models.DecimalField(max_digits=9, decimal_places=3, verbose_name="Precio",
                              help_text="Precio de venta con IVA")
    photo = models.ImageField(upload_to="item/", verbose_name="Foto", help_text="Foto principal del item.")
    description = models.TextField(verbose_name="Descripción", help_text="Descripción del item.", blank=True,
                                   default="")
    stock = models.BooleanField(default=True, verbose_name="Stock")

    def __str__(self) -> str:
        return f"[{self.sku}] {self.name}"

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        db_table = "item"


# @receiver(pre_save, sender=ItemModel)
# def set_code(sender, instance, **kwargs):
#     ref = ItemModel.objects.all().last().pk + 1
#
#     code = f"CODE-{ref}"
#     instance.sku = code
