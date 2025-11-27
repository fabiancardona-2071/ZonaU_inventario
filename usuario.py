from producto import *
class Usuario:
    def __init__(self,id_usuario,nombre,apellido,N_usuario,contraseña):
        self.id_usuario=id_usuario
        self.nombre=nombre
        self.apellido=apellido
        self.N_usuario=N_usuario
        self.contraseña=contraseña
        self.sesion_activa=False
    
    def iniciar_sesion(self,password):
        if self.N_usuario and self.contraseña==password:
            self.sesion_activa=True
            print("la sesion se ha iniciado correctamente")
        else:
            print("¡ERROR!: Usuario o contraseña incorrectos")
    def cerrar_sesion(self):
        if self.sesion_activa ==True:
            self.sesion_activa=False
            print("La sesion se ha cerrado con exito")
        else: 
            print("la sesion ya se encuentra cerrada")
    
class administrador(Usuario):
    def __init__(self, id_usuario, nombre, apellido, N_usuario, contraseña, codigo_jefe):
        super().__init__(id_usuario, nombre, apellido, N_usuario, contraseña)
        self.codigojefe=codigo_jefe
        self.usuarios={}
    def crear_usuario(self,user):
        self.usuarios[user.id_usuario]=user
        print("Usuario creado con exito")
    def eliminar_usuario(self,id_usuario):
        if id_usuario in self.usuarios:
            eliminado=self.usuarios.pop(id_usuario)
            print(f"Usuario {eliminado.nombre} fue eliminado")
        else: 
            print("El usuario no existe")
    def generar_reporte_completo(self):
        print("===== REPORTE COMPLETO DE USUARIOS =====")
        for u in self.usuarios.values():
            print(f"- {u.id_usuario} | {u.nombre} {u.apellido}")
        print("========================================")
class empleado(Usuario):
    def __init__(self, id_usuario, nombre, apellido, N_usuario, contraseña,area,inventario):
        super().__init__(id_usuario, nombre, apellido, N_usuario, contraseña)
        self.area=area
        self.inventario=inventario
    def buscar_producto(self,nombre_p):
        producto=self.inventario.buscar_producto(nombre_p)
        if producto:
            print(f"el producto encontrado: {producto.nombre_p} (stock: {producto.stock})")
        