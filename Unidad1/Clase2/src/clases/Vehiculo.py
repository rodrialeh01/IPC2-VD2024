class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.disponible = True
    
    def mantenimiento(self):
        self.disponible = False
    
    def disponibilizar(self):
        self.disponible = True
    
    def informacionDetallada(self):
        #: ^ centro
        #: < izquierda
        #: > derecha
        print(f"|{"Vehiculo":^61}|")
        # string * 3 = stringstringstring
        # "*" * 5 = *****
        print(f"|"+"-"*30 + "|"+"-"*30+"|")
        print(f"|{"Marca":<30}|{self.marca:<30}|")
        print(f"|{"Modelo":<30}|{self.modelo:<30}|")
        print(f"|{"Año":<30}|{self.anio:<30}|")
        print(f"|{"Disponible":<30}|{self.disponible:<30}|")
        print(f"|"+"-"*61+"|")
    
    # ENCAPSULAMIENTO
    # GETTERS
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo
    
    def getAnio(self):
        return self.anio
    
    def getDisponible(self):
        return self.disponible
    
    # SETTERS
    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setAnio(self, anio):
        self.anio = anio
    
    def setDisponible(self, disponible):
        self.disponible = disponible
