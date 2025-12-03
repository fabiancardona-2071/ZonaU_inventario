from producto import *
class Usuario:
    def __init__(self,id_usuario,nombre,apellido,N_usuario,contrasena,rol):
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.apellido=apellido
        self.N_usuario=N_usuario
        self.contrasena=contrasena
        self.sesion_activa=False
        self.rol=rol
    def cerrar_sesion(self):
        if self.sesion_activa:
            self.sesion_activa = False
            print("La sesión se ha cerrado con éxito")
        else:
            print("La sesión ya se encuentra cerrada")
    
class administrador(Usuario):
    def __init__(self, id_usuario, nombre, apellido, N_usuario, contrasena,rol, codigo_jefe):
        super().__init__(id_usuario, nombre, apellido, N_usuario, contrasena,rol)
        self.codigojefe=codigo_jefe
        self.usuarios={}

    def generar_reporte_completo(self):
        print("===== REPORTE COMPLETO DE USUARIOS =====")
        for u in self.usuarios.values():
            print(f"- {u.id_usuario} | {u.nombre} {u.apellido}")
        print("========================================")
class empleado(Usuario):
    def __init__(self, id_usuario, nombre, apellido, N_usuario, contrasena,rol,area,inventario):
        super().__init__(id_usuario, nombre, apellido, N_usuario, contrasena,rol)
        self.area=area
        self.inventario=inventario
    def buscar_producto(self,nombre_p):
        producto=self.inventario.buscar_producto(nombre_p)
        if producto:
            print(f"el producto encontrado: {producto.nombre_p} (stock: {producto.stock})")
        