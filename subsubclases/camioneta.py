from subclases.coches import Coche

class Camioneta(Coche):
    def _init_(self, color, ruedas, velocidad, cilindrada, carga):
        super()._init_(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def _str_(self):
        return super()._str_() + ", Carga: {} kg".format(self.carga)
    
    def catalogar(self, vehiculos):
        for vehiculo in vehiculos:
            print(type(vehiculo).__name__, vehiculo)