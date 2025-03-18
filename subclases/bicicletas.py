from superclases.vehiculo import Vehiculo
from subsubclases.motocicleta import Motocicleta
from subclases.bicicletas import Bicicleta


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, marchas):
        super().__init__(color, ruedas)
        self.marchas = marchas

    def __str__(self):
        return super().__str__() + f", {self.marchas} marchas"
    
    def catalogar(self, vehiculos):
         for vehiculo in vehiculos:
             print(type(vehiculo).__name__, vehiculo)
             
    # Crear lista de vehículos
vehiculos = [
    Motocicleta("Negra", 2, "Deportiva"),
    Bicicleta("Azul", 2, 18),
    Vehiculo("Blanco", 4)  # Un vehículo genérico
]