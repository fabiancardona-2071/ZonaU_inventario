from producto import Producto
from producto import movimientostok
from usuario import Usuario

class GestorStock:
    def __init__(self):
        self.lista_productos = {}
        self.lista_usuarios = {}
        self.movimientos_recientes = []
        self.id_movimiento_auto = 1


    # AGREGAR PRODUCTO

    def agregar_producto(self, producto: Producto):
        if producto.id_producto in self.lista_productos:
            print("❌ Error: El producto ya existe")
        else:
            self.lista_productos[producto.id_producto] = producto
            print("✔ Producto agregado correctamente")
    
    #BUSCAR PRODUCTO
    
    def buscar_producto(self, nombre_producto):
        for producto in self.lista_productos.values():
            if producto.nombre_p.lower() == nombre_producto.lower():
                return producto
        return None


    # ELIMINAR PRODUCTO POR ID

    def eliminar_producto(self, id_producto):
        if id_producto in self.lista_productos:
            eliminado = self.lista_productos.pop(id_producto)
            print(f"✔ Producto '{eliminado.nombre_p}' eliminado")
        else:
            print("❌ El producto no existe")


    # REGISTRAR MOVIMIENTO

    def registrar_movimiento(self, id_producto, tipo, cantidad, id_usuario):
        if id_producto not in self.lista_productos:
            print("❌ Producto no encontrado")
            return

    # crear movimiento con id_movimiento
        mov = movimientostok(
            self.id_movimiento_auto,   # id_movimiento (auto-incremental)
            id_producto,
            tipo,
            cantidad,
            id_usuario
        )
    # incrementar contador y guardar
        self.id_movimiento_auto += 1
        self.movimientos_recientes.append(mov)

        # Actualizar stock del producto
        producto = self.lista_productos[id_producto]
        if tipo == "ENTRADA":
            producto.stock += cantidad
        elif tipo == "SALIDA":
            producto.stock -= cantidad
        else:
            print("⚠ Tipo de movimiento no reconocido. Use 'ENTRADA' o 'SALIDA'.")
            return

        print("✔ Movimiento registrado")
    

    # REPORTE DE MOVIMIENTOS POR FECHA

    def obtener_reporte_movimientos(self, fecha_inicio, fecha_fin):
        print("===== REPORTE DE MOVIMIENTOS =====")
        for mov in self.movimientos_recientes:
            if fecha_inicio <= mov.fecha_hora.date() <= fecha_fin:
                print(mov)
        print("===================================")


    # ALERTAS STOCK MÍNIMO

    def alertas_stock_minimo(self, limite=5):
        print("===== ALERTAS DE STOCK MÍNIMO =====")
        for p in self.lista_productos.values():
            if p.stock <= limite:
                print(f"⚠ Producto {p.nombre_p} está bajo en stock ({p.stock})")
        print("====================================")

