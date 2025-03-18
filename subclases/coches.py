from superclases.vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f", {self.velocidad} km/h, {self.cilindrada} cc"
    
    def catalogar(self, vehiculos):
         for vehiculo in vehiculos:
             print(type(vehiculo).__name__, vehiculo)

# Crear lista de vehículos
vehiculos = [
    Coche("Rojo", 4, 180, 2000),
    Vehiculo("Blanco", 4)  # Un vehículo genérico
]