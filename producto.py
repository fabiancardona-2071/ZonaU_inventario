from datetime import datetime
class Producto:
    def __init__(self,id_producto,nombre_p,descripcion_p,proveedor,precio_costo,precio_venta,stock,fecha_ingreso):
        self.id_producto=id_producto
        self.nombre_p=nombre_p
        self.descripcion_p=descripcion_p
        self.proveedor=proveedor
        self.precio_costo=precio_costo
        self.precio_venta=precio_venta
        self.stock=stock
        self.fecha_ingreso=fecha_ingreso
    def actualizar_stock(self,cantidad):
        self.stock+=cantidad
        print("se ha cambiado el stock correctamente")
    def mostrar_info_producto(self):
        print("----- Información del Producto -----")
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre_p}")
        print(f"Categoría: {self.descripcion_p}")
        print(f"Stock: {self.stock}")
        print(f"Precio: {self.precio_venta}")
class gestor_producto:
    def __init__(self):
        self.productos={}
    def agregar_producto(self,producto):
        self.productos[producto.id_producto]=producto
    def buscar_producto(self,nombre):
        for p in self.productos.values():
            if p.nombre_p.lower()==nombre.lower():
                return p
        return None
class movimientostok:
    def __init__(self,id_movimiento,id_producto,tipo_movimiento,cantidad,id_usuario_responsable):
        self.id_movimiento=id_movimiento 
        self.id_producto = id_producto
        self.tipo_movimiento = tipo_movimiento   # "ENTRADA" o "SALIDA"
        self.cantidad = cantidad
        self.fecha_hora = datetime.now()
        self.id_usuario_responsable = id_usuario_responsable

    def registrar_movimiento(self):
        print("📦 MOVIMIENTO REGISTRADO")
        print(f"ID Movimiento: {self.id_movimiento}")
        print(f"Producto ID: {self.id_producto}")
        print(f"Tipo: {self.tipo_movimiento}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Fecha y Hora: {self.fecha_hora}")
        print(f"Usuario Responsable ID: {self.id_usuario_responsable}")
        print("-------------------------------------")
    def __str__(self):
        return (f"[{self.fecha_hora}] Movimiento {self.tipo_movimiento} | "
                f"MovID: {self.id_movimiento} | ProdID: {self.id_producto} | "
                f"Cantidad: {self.cantidad} | Usuario: {self.id_usuario_responsable}")