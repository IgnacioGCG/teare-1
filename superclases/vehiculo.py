class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas"
    
    def catalogar(vehiculo):
        for vehiculos in vehiculo:
            print(type(vehiculos).__name__, vehiculos)