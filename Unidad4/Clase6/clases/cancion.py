class Cancion:
    def __init__(self, id, titulo, artista, album, anio,genero,duracion):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.anio = anio
        self.genero = genero
        self.duracion = duracion
    
    def __str__(self):
        return f'ID: {self.id}\\n' \
        f'Titulo: {self.titulo}\\n' \
        f'Artista: {self.artista}\\n' \
        f'Album: {self.album}\\n' \
        f'Año: {self.anio}\\n' \
        f'Genero: {self.genero}\\n' \
        f'Duracion: {self.duracion}'