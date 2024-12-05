from clases.Vehiculo import Vehiculo


class Concesionario:
    def __init__(self):
        self.vehiculos = []
    
    def agregarVehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)
    
    def mostrarVehiculos(self):
        for vehiculo in self.vehiculos:
            vehiculo.informacionDetallada()
    
    def buscarPorMarca(self, marca):
        for vehiculo in self.vehiculos:
            if vehiculo.marca == marca:
                vehiculo.informacionDetallada()
    
    def eliminarVehiculo(self, modelo):
        for vehiculo in self.vehiculos:
            if vehiculo.modelo == modelo:
                self.vehiculos.remove(vehiculo)
    
    def mantenerVehiculo(self, modelo):
        for vehiculo in self.vehiculos:
            if vehiculo.modelo == modelo:
                vehiculo.mantenimiento()
    
    def disponibilizarVehiculo(self, modelo):
        for vehiculo in self.vehiculos:
            if vehiculo.modelo == modelo:
                vehiculo.disponibilizar()