class SolicitudCola:
    def __init__(self, id, ruta_xml, id_solicitante):
        self.id = id
        self.ruta_xml = ruta_xml
        self.id_solicitante = id_solicitante
    
    def __str__(self):
        return f'ID: {self.id}\\n'\
               f'XML: {self.ruta_xml}\\n'\
               f'ID Solicitante: {self.id_solicitante}'