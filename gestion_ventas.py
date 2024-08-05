import json
from datetime import datetime

class Venta:
    def __init__(self, fecha, cliente, productos):
        self.fecha = fecha
        self.cliente = cliente
        self.productos = productos

    def to_dict(self):
        return {
            'fecha': self.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'cliente': self.cliente,
            'productos': self.productos
        }

class VentaOnline(Venta):
    def __init__(self, fecha, cliente, productos, direccion_envio, metodo_pago):
        super().__init__(fecha, cliente, productos)
        self.direccion_envio = direccion_envio
        self.metodo_pago = metodo_pago

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'direccion_envio': self.direccion_envio,
            'metodo_pago': self.metodo_pago,
            'tipo': 'online'
        })
        return data

class VentaLocal(Venta):
    def __init__(self, fecha, cliente, productos, cajero, tienda):
        super().__init__(fecha, cliente, productos)
        self.cajero = cajero
        self.tienda = tienda

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'cajero': self.cajero,
            'tienda': self.tienda,
            'tipo': 'local'
        })
        return data

class SistemaGestionVtas:
    def __init__(self, archivo):
        self.archivo = archivo
        self.ventas = self.cargar_ventas()

    def cargar_ventas(self):
        try:
            with open(self.archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def guardar_ventas(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.ventas, f, indent=4)

    def agregar_venta(self, venta):
        self.ventas.append(venta.to_dict())
        self.guardar_ventas()

    def obtener_venta(self, index):
        try:
            return self.ventas[index]
        except IndexError:
            print("Índice fuera de rango")
            return None

    def actualizar_venta(self, index, venta):
        try:
            self.ventas[index] = venta.to_dict()
            self.guardar_ventas()
        except IndexError:
            print("Índice fuera de rango")

    def eliminar_venta(self, index):
        try:
            self.ventas.pop(index)
            self.guardar_ventas()
        except IndexError:
            print("Índice fuera de rango")

    def borrar_todas_ventas(self):
        self.ventas = []
        self.guardar_ventas()
        print("Todas las ventas han sido borradas.")