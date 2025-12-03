
from producto import *
from usuario import *
from gestor import *
from datetime import *
gestor= GestorStock()

admin_default = administrador(
    id_usuario="1",
    nombre="Admin",
    apellido="Principal",
    N_usuario="admin",
    contrasena="admin123",
    codigo_jefe="999",
    rol="admin"
)

empleado_default = empleado(
    id_usuario="2",
    nombre="Empleado",
    apellido="General",
    N_usuario="empleado",
    contrasena="empleado123",
    area="Almacén",
    inventario=gestor,
    rol="empleado"
)

gestor.lista_usuarios["1"] = admin_default
gestor.lista_usuarios["2"] = empleado_default


# ==========================================
# FUNCIÓN INICIO DE SESIÓN
# ==========================================

def iniciar_sesion():
    print("\n===== INICIO DE SESIÓN =====")
    user = input("Usuario: ")
    password = input("Contraseña: ")

    for u in gestor.lista_usuarios.values():
        if u.N_usuario == user and u.contrasena == password:
            u.sesion_activa = True
            print(f"✔ Bienvenido {u.nombre} ({u.rol.upper()})")
            return u

    print("❌ Usuario o contraseña incorrectos")
    return None





# ==========================================
# MENÚ ADMINISTRADOR
# ==========================================

def menu_admin(admin_logeado):

    while True:
        print("""
========== MENÚ ADMINISTRADOR ==========
1. Crear usuario
2. Eliminar usuario
3. Reporte completo de usuarios
4. Agregar producto
5. Eliminar producto
6. Registrar movimiento
7. Reporte de movimientos
8. Mostrar alertas de stock mínimo
9. Mostrar productos
10. Cerrar sesión
11. salir del programa
""")

        op = input("Seleccione una opción: ")

        # ===================================
        # USUARIOS
        # ===================================
        if op == "1":
            print("\n--- Crear Usuario ---")
            id_u = input("ID Usuario: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            user = input("Usuario: ")
            password = input("Contraseña: ")
            rol=input("rol: empleado/admin")
            nuevo = Usuario(id_u, nombre, apellido, user, password,rol)
            admin_logeado.crear_usuario(nuevo)

        elif op == "2":
            print("\n--- Eliminar Usuario ---")
            id_u = input("ID usuario a eliminar: ")
            admin_logeado.eliminar_usuario(id_u)

        elif op == "3":
            admin_logeado.generar_reporte_completo()

        # ===================================
        # PRODUCTOS
        # ===================================
        elif op == "4":
            print("\n--- Agregar Producto ---")
            id_p = input("ID: ")
            nombre = input("Nombre: ")
            desc = input("Descripción: ")
            prov = input("Proveedor: ")
            pcosto = float(input("Precio costo: "))
            pventa = float(input("Precio venta: "))
            stock = int(input("Stock inicial: "))
            fecha = datetime.now().date()

            prod = Producto(id_p, nombre, desc, prov, pcosto, pventa, stock, fecha)
            gestor.agregar_producto(prod)

        elif op == "5":
            id_p = input("ID del producto a eliminar: ")
            gestor.eliminar_producto(id_p)

        # ===================================
        # MOVIMIENTOS
        # ===================================
        elif op == "6":
            print("\n--- Registrar Movimiento ---")
            id_p = input("ID Producto: ")
            tipo = input("Tipo (ENTRADA/SALIDA): ").upper()
            cantidad = int(input("Cantidad: "))
            gestor.registrar_movimiento(id_p, tipo, cantidad, admin_logeado.id_usuario)

        elif op == "7":
            print("\n--- Reporte Movimientos ---")
            f1 = input("Fecha inicio YYYY-MM-DD: ")
            f2 = input("Fecha fin YYYY-MM-DD: ")
            gestor.obtener_reporte_movimientos(
                date.fromisoformat(f1),
                date.fromisoformat(f2)
            )

        # ===================================
        # ALERTAS & MOSTRAR PRODUCTOS
        # ===================================
        elif op == "8":
            limite = int(input("Límite de stock: "))
            gestor.alertas_stock_minimo(limite)

        elif op == "9":
            print("\n--- LISTA DE PRODUCTOS ---")
            for p in gestor.lista_productos.values():
                p.mostrar_info_producto()

        # ===================================
        # CERRAR SESIÓN
        # ===================================
        elif op == "10":
            admin_logeado.cerrar_sesion()
            break
        elif op=="11":
            print(" Cerrando programa...")
            exit() 

        else:
            print("❌ Opción inválida.")


# ==========================================
# MENÚ EMPLEADO
# ==========================================

def menu_empleado(emp):

    while True:
        print("""
============= MENÚ EMPLEADO =============
1. Buscar producto
2. Registrar movimiento
3. Mostrar productos
4. Cerrar sesión
5. salir del programa
""")

        op = input("Seleccione una opción: ")

        if op == "1":
            nombre = input("Nombre del producto: ")
            emp.buscar_producto(nombre)

        elif op == "2":
            print("\n--- Registrar Movimiento ---")
            id_p = input("ID Producto: ")
            tipo = input("Tipo (ENTRADA/SALIDA): ").upper()
            cantidad = int(input("Cantidad: "))
            gestor.registrar_movimiento(id_p, tipo, cantidad, emp.id_usuario)

        elif op == "3":
            for p in gestor.lista_productos.values():
                p.mostrar_info_producto()

        elif op == "4":
            emp.cerrar_sesion()
            break
        elif op=="5":
            print(" Cerrando programa...")
            exit()      

        else:
            print("Opción inválida.")


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def programa():
    while True:
        usuario_logeado = iniciar_sesion()

        if usuario_logeado:
            if usuario_logeado.rol=="admin":
                menu_admin(usuario_logeado)
            elif usuario_logeado.rol=="empleado":
                menu_empleado(usuario_logeado)


# EJECUTAR SISTEMA
programa()