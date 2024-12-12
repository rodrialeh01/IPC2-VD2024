from estructuras.lista_simple_circular.ListaCircular import ListaCircular


class Artista:
    def __init__(self, id, password, nombre, correo, telefono, especialidades, notasAdicionales):
        self.id = id
        self.password = password
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.especialidades = especialidades
        self.notasAdicionales = notasAdicionales
        self.procesadas = ListaCircular()

    def __str__(self):
        return f'ID: {self.id}\\n'\
               f'Password: {self.password}\\n'\
               f'Nombre: {self.nombre}\\n'\
               f'Correo: {self.correo}\\n'\
               f'Telefono: {self.telefono}\\n'\
               f'Especialidades: {self.especialidades}\\n'\
               f'Notas Adicionales: {self.notasAdicionales}'
    
    def insertarProcesadas(self, valor):
        self.procesadas.insertar(valor)