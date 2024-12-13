class SolicitudPila:
    def __init__(self, id, ruta_xml):
        self.id = id
        self.ruta_xml = ruta_xml
    
    def __str__(self):
        return f'ID: {self.id}\\n'\
               f'XML: {self.ruta_xml}\\n'