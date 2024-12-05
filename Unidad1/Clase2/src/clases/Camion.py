from clases.Vehiculo import Vehiculo


class Camion(Vehiculo):
    def __init__(self, marca,modelo,anio, capacidadCarga):
        super().__init__(marca,modelo,anio)
        self.capacidadCarga = capacidadCarga
    
    def informacionDetallada(self):
        #: ^ centro
        #: < izquierda
        #: > derecha
        print(f"|{"Camion":^61}|")
        # string * 3 = stringstringstring
        # "*" * 5 = *****
        print(f"|"+"-"*30 + "|"+"-"*30+"|")
        print(f"|{"Marca":<30}|{self.marca:<30}|")
        print(f"|{"Modelo":<30}|{self.modelo:<30}|")
        print(f"|{"Año":<30}|{self.anio:<30}|")
        print(f"|{"Disponible":<30}|{self.disponible:<30}|")
        print(f"|{"Capacidad":<30}|{self.capacidadCarga:<30}|")
        print(f"|"+"-"*61+"|")
    
    # ENCAPSULAMIENTO

    # GETTERS
    def getCapacidadCarga(self):
        return self.capacidadCarga

    # SETTERS
    def setCapacidadCarga(self, capacidadCarga):
        self.capacidadCarga = capacidadCarga