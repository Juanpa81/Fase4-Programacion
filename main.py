# Sistema de gestión - Fase 4

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Cédula:", self.cedula)


# Prueba del sistema
cliente1 = Cliente("Juan", "123456")

cliente1.mostrar_datos()


# Clase Servicio (Clase Base)


class Servicio:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_servicio(self):
        print("Servicio:", self.nombre)
        print("Precio:", self.precio)


