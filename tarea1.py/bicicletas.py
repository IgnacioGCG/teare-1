class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"Color {self.color}, {self.ruedas} ruedas"

class Moto(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo  # Deportiva, Turismo, etc.

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, marchas):
        super().__init__(color, ruedas)
        self.marchas = marchas

    def __str__(self):
        return super().__str__() + f", {self.marchas} marchas"
    # Crear lista de vehículos
vehiculos = [
    Moto("Negra", 2, "Deportiva"),
    Bicicleta("Azul", 2, 18),
    Vehiculo("Blanco", 4)  # Un vehículo genérico
]


# Función catalogar()
def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(filtrados)} vehículos con {ruedas} ruedas:")
        for v in filtrados:
            print(f"  - {type(v).__name__}: {v}")
    else:
        for v in vehiculos:
            print(f"{type(v).__name__}: {v}")


# Probar la función
print("\nTodos los vehículos:")
catalogar(vehiculos)

print("\nVehículos con 2 ruedas:")
catalogar(vehiculos, 2)

print("\nVehículos con 4 ruedas:")
catalogar(vehiculos, 4)