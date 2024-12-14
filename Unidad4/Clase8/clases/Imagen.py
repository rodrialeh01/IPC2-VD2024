class Imagen:
    def __init__(self, id, nombre, ruta_imagen):
        self.id = id
        self.nombre = nombre
        self.ruta_imagen = ruta_imagen
    
    def __str__(self):
        return f'ID: {self.id}\\n'\
               f'Nombre: {self.nombre}\\n'\
               f'Ruta imagen: {self.ruta_imagen}\\n'