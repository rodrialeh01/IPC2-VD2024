from clases.Imagen import Imagen
from estructuras.lista_doble_circular.ListaDobleCircular import \
    ListaDobleCircular


class Solicitante:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.id_galeria = 0
        self.galeria = ListaDobleCircular()
    
    def agregar_a_galeria(self, imagen):
        nuevo = Imagen(self.id_galeria,imagen)
        self.galeria.insertar(nuevo)
        self.id_galeria += 1
    
    def obtenerAnterior(self,id):
        return self.obtenerAnterior(id)