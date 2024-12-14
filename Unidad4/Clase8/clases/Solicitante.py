from estructuras.lista_doble_circular.ListaDobleCircular import \
    ListaDobleCircular
from estructuras.pila.pila import Pila


class Solicitante:
    def __init__(self, id, password, nombre, correo, telefono, direccion):
        self.id = id
        self.password = password
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.imagenes = ListaDobleCircular()
        self.pila = Pila()
    
    def __str__(self):
        return f'ID: {self.id}\\n'\
               f'Password: {self.password}\\n'\
               f'Nombre: {self.nombre}\\n'\
               f'Correo: {self.correo}\\n'\
               f'Telefono: {self.telefono}\\n'\
               f'Direccion: {self.direccion}'

    def pushPila(self, valor):
        self.pila.push(valor)
    
    def popPila(self):
        return self.pila.pop()
    
    def insertarImagen(self, imagen):
        self.imagenes.insertar(imagen)