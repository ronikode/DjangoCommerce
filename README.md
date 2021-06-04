### Django ecommerce

## Install

1.- Activar entorno virtual
2.- Instalar dependias del proyecto
3.- Ejecutar proyecto


### MODELS - ORM

 SQL `select * from item where stock=True;`

 QUERIES

 - ItemModel.objects.filter(stock=True)
 - ItemModel.objects.all()
 - ItemModel.objects.order_by("name")
 - ItemModel.objects.filter(stock=True).count()
 - ItemModel.objects.filter(pvp__gte=100).exists() | >= | True or False
 - ItemModel.objects.filter(pvp__lte=100).exists() | <= | True or False
 - instance, created = ItemModel.objects.get_or_create(name="Item c", sku="C0003", pvp=10) | (<ItemModel: [C0003] Item c>, True)

 BULKS
 items = [ItemModel(), ItemModel(), ItemModel(), ItemModel(), ItemModel()]
 ItemModel.objects.bulk_create(items)

 DELETE
 - ItemModel.objects.filter(stock=False).delete()




## MIGRACIONES

 - MAKEMIGRATIONS:

   `python manage.py makemigrations <name-app>`

 - MIGRATE:

    `python manage.py migrate <name-app>`