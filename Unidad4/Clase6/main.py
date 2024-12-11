#Element Tree
import xml.etree.ElementTree as ET
# Importar Tkinter para obtener la ruta de los archivos XML
from tkinter import filedialog, messagebox

from clases.cancion import Cancion
from estructuras.lista_doble_circular.ListaDobleCircular import \
    ListaDobleCircular
from estructuras.lista_simple_circular.ListaCircular import ListaCircular

canciones1 = ListaCircular()
canciones2 = ListaDobleCircular()


def menu():
    opcion = 0
    while True:
        print('------------LISTAS-------------')
        print('1. Carga masiva')
        print('2. Ver lista simple circular')
        print('3. Ver lista doblemente circular')
        print('4. Obtener anterior')
        print('5. Obtener siguiente')
        print('6. Salir')
        opcion = input('Ingrese la opción que desee: ')
        if opcion == '1':
            carga_masiva()
        elif opcion == '2':
            canciones1.graficar()
        elif opcion == '3':
            canciones2.graficar()
        elif opcion == '4':
            id_song = input('Ingrese el ID de la cancion que desee obtener: ')
            song = canciones2.obtenerAnterior(id_song)
            print('----------- LA ANTERIOR CANCION ES--------------')
            print('ID: ', song.id)
            print('Titulo: ', song.titulo)
            print('Artista: ', song.artista)
        elif opcion == '5':
            id_cancion = input('Ingrese el ID de la cancion que desee obtener: ')
            cancion = canciones2.obtenerSiguiente(id_cancion)
            print('----------- LA SIGUIENTE CANCION ES--------------')
            print('ID: ', cancion.id)
            print('Titulo: ', cancion.titulo)
            print('Artista: ', cancion.artista)
        elif opcion == '6':
            break
        else:
            print('Opción no válida')

def carga_masiva():
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    if root.tag == 'musica':
        contador_id = 0
        for cancion in root:
            titulo = ''
            artista = ''
            album = ''
            anio = ''
            genero = ''
            duracion = ''
            for hijo in cancion:
                if hijo.tag == 'titulo':
                    titulo = hijo.text
                elif hijo.tag == 'artista':
                    artista = hijo.text
                elif hijo.tag == 'album':
                    album = hijo.text
                elif hijo.tag == 'anio':
                    anio = hijo.text
                elif hijo.tag == 'genero':
                    genero = hijo.text
                elif hijo.tag == 'duracion':
                    duracion = hijo.text
            nueva_cancion = Cancion(str(contador_id),titulo,artista,album,anio,genero,duracion)
            canciones1.insertar(nueva_cancion)
            canciones2.insertar(nueva_cancion)
            contador_id += 1

if __name__ == '__main__':
    menu()