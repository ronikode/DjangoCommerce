# CREAR CLASE DE ORDENES O PEDIDOS CON LA SIGUIENTE INFORMACION
# ODER (crated_at, code, warehouse, items, total_quantity, total_amount)
# class Order

# Importa modulos de python
import datetime
from decimal import Decimal
import uuid
from random import randrange

products = [
    {'name': "item a", 'pvp': 10, 'bodega': 'A'},
    {'name': "item b", 'pvp': 20, 'bodega': 'A'},
    {'name': "item c", 'pvp': 30, 'bodega': 'B'},
    {'name': "item d", 'pvp': 40, 'bodega': 'C'},
    {'name': "item e", 'pvp': 5, 'bodega': 'B'}
]


def generate_unique_code():
    """Function that generate unique code"""
    # .strftime("%Y-%m-%d-%H-%S-%f")
    frame = datetime.datetime.now().strftime("%S%f")  # Dado una fecha actual (objeto datetime)
    code = str(uuid.uuid4()).split("-")
    unique_code = f"{code[0]}{frame}"
    return unique_code


class OrderModel:

    # metodo constructor
    def __init__(self, created_at: datetime,
                 warehouse: dict, items: []):
        self.created_at = created_at
        # self.code = randrange(1000, 9999, 2)
        self.code = generate_unique_code()
        self.warehouse = warehouse
        self.items = items
        self.total_qty = 0
        self.total_amount = 0

    # DONE: 1) Implementar metodo cantidad de items
    # DONE: 2) Implementar total en monto de items

    # METODOS DE INSTANCIA
    def set_total_quantity(self):
        self.total_qty = len(self.items)

    def set_total_amount(self):
        total = 0
        for item in self.items:
            total += item.get('pvp')
        self.total_amount = total

    # DONE: 3) Crear una funcion que me genere codigo unico (random) y sea seteado en el pedido/orden.
    # PEP 8
    # def get_codigo(self):
    #     self.code = randrange(1000, 9999, 2)

    # METODOS ESTATICOS


warehouse_a = {"code": "A", "name": "Bodega A"}

order_a = OrderModel(created_at=datetime.datetime.now(), warehouse=warehouse_a, items=products)
order_a.set_total_quantity()
order_a.set_total_amount()
order_b = OrderModel(created_at=datetime.datetime.now(), warehouse=warehouse_a, items=[])
print(f"Orden: {order_b.code}")
print(f"La cantidad de items {order_a.total_qty}")
print(f"Total del pedido: {order_a.code} es $: {order_a.total_amount}")
