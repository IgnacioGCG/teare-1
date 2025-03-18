
# Crear lista de vehículos
vehiculos = [
    Coche("Rojo", 4, 180, 2000),
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
