# Identifica tres tipos de usuarios de su aplicación.
# Identifica tres atributos por tipo de usuario.
# Identifica tres acciones que pueden desarrollar cada tipo de usuario. Las acciones se deben ejecutar de
# forma interna en nuestra aplicación. Por ejemplo, acceder a datos sensibles, registrar nuevos usuarios,
# enviar solicitudes de información adicional.
# ● Piense en nuevos atributos y acciones que pueden realizar los objetos.
# Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
# gráfica. Desarrollen el ejercicio de forma intuitiva.
class Persona:
    def __init__(self, tipo):
        self.tipo = tipo


class Administrador(Persona):
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def ingresar(self):
        print(" ha ingresado como administrador")

    def modificar(self):
        print("como puede modificar todo el sistema")


class Usuario(Persona):
    def __init__(self, nombre, correo, password):
        self.nombre = nombre
        self.correo = correo
        self.password = password

    def ingresar(self):
        print("ha ingresado como usuario normal")

    def ingresar_datos(self):
        print("solo puede ingresar datos")

    def comprar(self, producto, cantidad, precio):
        print("usted a comprado ciertas canitdad de productos")


class Invitado(Persona):
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def ingresar(self):
        print("ha ingresado con privilegios de invitado")

    def ver_datos(self):
        print("solo puede ver datos en este usuario")

class CarritoCompra:
    def __init__(self, nombre, categoria, precio, cantidad = 1):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

    def stock(self):
        print(f"el producto {self.nombre} tiene un stock de {self.cantidad}")

producto1 = CarritoCompra('martillo', 'ferreteria', 'hogar', 1000)

producto1.stock()



