# DADO LISTA DE ITEMS
items = [
    {'name': "item a", 'pvp': 10, 'bodega': 'A'},
    {'name': "item b", 'pvp': 20, 'bodega': 'A'},
    {'name': "item c", 'pvp': 30, 'bodega': 'B'},
    {'name': "item d", 'pvp': 40, 'bodega': 'C'},
    {'name': "item e", 'pvp': 5, 'bodega': 'B'}
]


# 1.- AGRUPAR POR BODEGAS MOSTRAR TODOS LOS ITEMS DE BODEGA A Y C
def items_by_warehouse(products: list, name_warehouse: str = ''):
    # product.get("YYY", "") => None
    message = ""
    for product in products:
        if product.get("bodega") == 'A' or product.get("bodega") == 'C':
            # c = product.get("YYY")
            # if c is None:
            #     print("parametro no disponible de items")
            message = message + "\n" + product.get("name")
    return message


# LIST COMPREHENSION
result = [item.get('name') for item in items if item.get("bodega") == 'A' or item.get("bodega") == 'C']
print(result)
response = items_by_warehouse(products=items)
print(response)


# 2.- MOSTRAR EL TOTAL $ (MONTO O pvp) de items que se encuentra en la BODEGA B.
def total_by_warehouse(products: list):
    messaje = ""
    total = 0
    for product in products:
        if product.get("bodega") == 'B':
            messaje = messaje + "\n" + product.get('name')
            total = total + product.get('pvp')
    messaje = messaje + f"\n Total de PVP {total}"
    return messaje


result = total_by_warehouse(products=items)
print(result)
