class Vehiculo:
    def _init_(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def _str_(self):
        return "Color: {}, Ruedas: {}".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def _init_(self, color, ruedas, velocidad, cilindrada):
        super()._init_(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def _str_(self):
        return super()._str_() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)

class Bicicleta(Vehiculo):
    def _init_(self, color, ruedas, tipo):
        super()._init_(color, ruedas)
        self.tipo = tipo
    
    def _str_(self):
        return super()._str_() + ", Tipo: {}".format(self.tipo)

class Camioneta(Coche):
    def _init_(self, color, ruedas, velocidad, cilindrada, carga):
        super()._init_(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def _str_(self):
        return super()._str_() + ", Carga: {} kg".format(self.carga)

class Motocicleta(Bicicleta):
    def _init_(self, color, ruedas, tipo, velocidad, cilindrada):
        super()._init_(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def _str_(self):
        return super()._str_() + ", Velocidad: {} km/h, Cilindrada: {} cc".format(self.velocidad, self.cilindrada)

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in filtrados:
            print(type(vehiculo)._name_, ":", vehiculo)
    else:
        for vehiculo in vehiculos:
            print(type(vehiculo)._name_, ":", vehiculo)

# Creación de objetos y lista de vehículos
vehiculos = [
    Coche("Rojo", 4, 180, 2000),
    Bicicleta("Azul", 2, "Urbana"),
    Camioneta("Blanco", 4, 160, 2500, 1000),
    Motocicleta("Negro", 2, "Deportiva", 220, 1000)
]

# Pruebas de catalogar
print("\nTodos los vehículos:")
catalogar(vehiculos)
print("\nVehículos con 2 ruedas:")
catalogar(vehiculos, 2)
print("\nVehículos con 4 ruedas:")
catalogar(vehiculos, 4)