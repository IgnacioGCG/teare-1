from subclases.bicicletas import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo  # Deportiva, Turismo, etc.

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"
    
    def catalogar(self, vehiculos):
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__, vehiculo)