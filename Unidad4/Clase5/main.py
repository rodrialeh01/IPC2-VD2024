#Element Tree
import xml.etree.ElementTree as ET
# Importar Tkinter para obtener la ruta de los archivos XML
from tkinter import filedialog, messagebox

from clases.libro import Libro
from clases.usuario import Usuario
from estructuras.lista_doble.listaDoble import ListaDoble
from estructuras.lista_simple.listaSimple import ListaSimple

lista_usuarios = ListaSimple()
lista_libros = ListaDoble()

def menu():
    opcion = 0
    while True:
        print('------------LISTAS-------------')
        print('1. Carga masiva')
        print('2. Ver lista simple enlazada')
        print('3. Ver lista doblemente enlazada')
        print('4. Obtener libro')
        print('5. Obtener usuario')
        print('6. Validar que tipo es')
        print('7. Salir')
        opcion = input('Ingrese la opción que desee: ')
        if opcion == '1':
            carga_masiva()
        elif opcion == '2':
            lista_usuarios.graficar()
        elif opcion == '3':
            lista_libros.graficar()
        elif opcion == '4':
            id_libro = input('Ingrese el ID del libro que desee obtener: ')
            libro = lista_libros.buscar(id_libro)
            if libro != None:
                print(str(libro))
        elif opcion == '5':
            id_user = input('Ingrese el ID del usuario: ')
            usuario = lista_usuarios.obtenerUsuario(id_user)
            if usuario != None:
                print(str(usuario))
            else:
                print('No se encontró el usuario')
        elif opcion == '6':
            validar()
        elif opcion == '7':
            break
        else:
            print('Opción no válida')

def carga_masiva():
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    if root.tag == 'usuarios':
        for usuario in root:
            id = usuario.attrib['id']
            password = usuario.attrib['password']
            nombre = ''
            edad = ''
            correo = ''
            telefono = ''
            for hijo in usuario:
                if hijo.tag == 'nombre':
                    nombre = hijo.text
                elif hijo.tag == 'edad':
                    edad = hijo.text
                elif hijo.tag == 'email':
                    correo = hijo.text
                elif hijo.tag == 'telefono':
                    telefono = hijo.text
            nuevo = Usuario(id,password,nombre,edad,correo,telefono)
            lista_usuarios.insertar(nuevo)
    elif root.tag == 'libros':
        for libro in root:
            id = libro.attrib['id']
            titulo = ''
            autor = ''
            precio = ''
            imagen = ''
            for hijo in libro:
                if hijo.tag == 'titulo':
                    titulo = hijo.text
                elif hijo.tag == 'autor':
                    autor = hijo.text
                elif hijo.tag == 'precio':
                    precio = hijo.text
                elif hijo.tag == 'imagen':
                    imagen = hijo.text
            nuevo_libro = Libro(id,titulo,autor,precio,imagen)
            lista_libros.insertar(nuevo_libro)

def validar():
    texto = input('Ingresa un código: ')
    #ART
    if texto == 'AdminIPC':
        print('Bienvenido Administrador')
    elif texto[0] == 'A' and texto[1] == 'R' and texto[2] == 'T':
        print('Es un artista')
    elif texto[0] == 'I' and texto[1] == 'P' and texto[2] == 'C':
        print('Es un solicitante')

if __name__ == '__main__':
    menu()