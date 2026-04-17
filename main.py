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



# Clase Sala (Hereda de Servicio)


class Sala(Servicio):
    def __init__(self, nombre, precio, capacidad):
        super().__init__(nombre, precio)
        self.capacidad = capacidad

    def mostrar_servicio(self):
        super().mostrar_servicio()
        print("Capacidad:", self.capacidad)



# Clase Equipo (Hereda de Servicio)


class Equipo(Servicio):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def mostrar_servicio(self):
        super().mostrar_servicio()
        print("Tipo:", self.tipo)



# Clase Asesoria (Hereda de Servicio)


class Asesoria(Servicio):
    def __init__(self, nombre, precio, especialista):
        super().__init__(nombre, precio)
        self.especialista = especialista

    def mostrar_servicio(self):
        super().mostrar_servicio()
        print("Especialista:", self.especialista)


# Pueba de Funcionamiento


servicio1 = Sala("Sala de reuniones", 50000, 10)
servicio2 = Equipo("Computador", 30000, "Tecnología")
servicio3 = Asesoria("Asesoría IT", 80000, "Ingeniero")

servicio1.mostrar_servicio()
servicio2.mostrar_servicio()
servicio3.mostrar_servicio()
