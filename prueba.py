
from producto import Producto
from usuario import Usuario
from gestor import GestorStock
from datetime import date

gestor = GestorStock()

# Usuarios
u1 = Usuario(1, "Fabian", "Cardona", "fcardona", "1234")
gestor.lista_usuarios[u1.id_usuario] = u1

# Productos
p1 = Producto(101, "Mouse Gamer", "Mouse RGB 7200 DPI", "TechStore", 30000, 60000, 8, "2025-02-01")
p2 = Producto(102, "Teclado Mecánico", "Teclado Blue Switch", "TechStore", 80000, 150000, 3, "2025-02-02")
gestor.agregar_producto(p1)
gestor.agregar_producto(p2)

# Movimientos
gestor.registrar_movimiento(101, "SALIDA", 2, 1)
gestor.registrar_movimiento(102, "ENTRADA", 5, 1)

# Reporte
gestor.obtener_reporte_movimientos(date.today(), date.today())

# Alertas
gestor.alertas_stock_minimo(limite=5)
