class Animal:
    def __init__(self, nombre, velocidad, cobertura):
        self.nombre = nombre
        self.velocidad = velocidad
        self.cobertura = cobertura

    def saludar(self):
        print(f"hola!! mo nombre es {self.nombre}")

    def desplazar(self, tiempo):
        distancia = self.velocidad * tiempo
        print(f"la distancia recorrida es {distancia} kilometros")


class Pajaro(Animal):
    pass


class Perro(Animal):
    pass


pajaro1 = Pajaro("piolin", 15, "plumaje")
perro1 = Perro("hector", 30, "pelaje")

pajaro1.nombre
perro1.nombre
pajaro1.velocidad
perro1.velocidad
pajaro1.saludar()
perro1.saludar()
pajaro1.desplazar(0.5)
perro1.desplazar(2)
