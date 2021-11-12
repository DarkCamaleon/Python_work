# Identifica tres tipos de usuarios de su aplicación.
# Identifica tres atributos por tipo de usuario.
# Identifica tres acciones que pueden desarrollar cada tipo de usuario. Las acciones se deben ejecutar de
# forma interna en nuestra aplicación. Por ejemplo, acceder a datos sensibles, registrar nuevos usuarios,
# enviar solicitudes de información adicional.
# ● Piense en nuevos atributos y acciones que pueden realizar los objetos.
# Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
# gráfica. Desarrollen el ejercicio de forma intuitiva.

class Administrador:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def ingresar():
        print(" ha ingresado como administrador")

    def modificar():
        print("como puede modificar todo el sistema")


class usuario:
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def ingresar():
        print("ha ingresado como usuario normal")

    def ingresar_datos():
        print("solo puede ingresar datos")

    def comprar(producto, cantidad, precio):
        print("usted a comprado ciertas canitdad de productos")


class invitado:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def ingresar():
        print("ha ingresado con privilegios de invitado")

    def ver_datos():
        print("solo puede ver datos en este usuario")

class Producto:
    def __init__(self, nombre, categoria, precio, cantidad = 1):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad


