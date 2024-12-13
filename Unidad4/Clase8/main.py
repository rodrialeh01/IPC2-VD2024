#Element Tree
import xml.etree.ElementTree as ET
# Importar Tkinter para obtener la ruta de los archivos XML
from tkinter import filedialog, messagebox

from clases.Artista import Artista
from clases.Imagen import Imagen
from clases.Solicitante import Solicitante
from clases.SolicitudCola import SolicitudCola
from clases.SolicitudPila import SolicitudPila
from estructuras.estructuras import (colaSolicitudes, id_logueado,
                                     listaArtistas, listaSolicitantes)
from estructuras.matrizDispersa.matrizDispersa import MatrizDispersa


def inicio():
    global id_logueado
    while True:
        print("----------------PIXIPC2-------------------")
        print("-----------------LOGIN--------------------")
        id = input("Ingresa tu ID: ")
        pwd = input("Ingresa tu contrasenia: ")
        if id == "admin" and pwd == "admin":
            print("Bienvenido administrador")
            MenuAdmin()
        elif id.startswith("ART-") and listaArtistas.loginUsuario(id,pwd) == True:
            id_logueado = id
            MenuArtista()
        elif id.startswith("IPC-") and listaSolicitantes.login(id,pwd) == True:
            id_logueado = id
            MenuSolicitante()
        else:
            print("Usuario o contraseña incorrectos")

def MenuAdmin():
    while True:
        print("-------------ADMINISTRADOR---------------")
        print("1. Cargar Solicitantes")
        print("2. Cargar Artistas")
        print("3. Cerrar Sesión")
        opcion = input("> ")
        if opcion == "1":
            CargarSolicitantes()
        elif opcion == "2":
            CargarArtistas()
        elif opcion == "3":
            break

def CargarSolicitantes():
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    if root.tag == "solicitantes":
        for solicitante in root:
            id = solicitante.attrib["id"]
            pwd = solicitante.attrib["pwd"]
            nombre = ''
            correo = ''
            telefono = ''
            direccion = ''
            for hijo in solicitante:
                if hijo.tag == "NombreCompleto":
                    nombre = hijo.text
                elif hijo.tag == "CorreoElectronico":
                    correo = hijo.text
                elif hijo.tag == "NumeroTelefono":
                    telefono = hijo.text
                elif hijo.tag == "Direccion":
                    direccion = hijo.text
            nuevo_solicitante = Solicitante(id,pwd,nombre,correo,telefono,direccion)
            listaSolicitantes.insertar(nuevo_solicitante)

def CargarArtistas():
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    if root.tag == "Artistas":
        for artista in root:
            id = artista.attrib["id"]
            pwd = artista.attrib["pwd"]
            nombre = ''
            correo = ''
            telefono = ''
            especialidades = ''
            notas = ''
            for hijo in artista:
                if hijo.tag == "NombreCompleto":
                    nombre = hijo.text
                elif hijo.tag == "CorreoElectronico":
                    correo = hijo.text
                elif hijo.tag == "NumeroTelefono":
                    telefono = hijo.text
                elif hijo.tag == "Especialidades":
                    especialidades = hijo.text
                elif hijo.tag == "NotasAdicionales":
                    notas = hijo.text
            nuevo_artista = Artista(id,pwd,nombre,correo,telefono,especialidades,notas)
            listaArtistas.insertar(nuevo_artista)

def MenuArtista():
    global id_logueado
    while True:
        print('--------------MENU ARTISTA--------------------')
        print('-------------SOLICITUDES EN COLA--------------')
        if colaSolicitudes.verPrimero() == None:
            print('---------------NO HAY SOLICITUDES------------')
        else:
            solicitud = colaSolicitudes.verPrimero()
            print(f'------------SOLICITUD ID: {solicitud.id}---------------')
            print(f'Ruta XML: {solicitud.ruta_xml}')
            print(f'Solicitante: {solicitud.id_solicitante}')
            print('------------------------------------------------')
        print('')
        print('-----------------OPCIONES-----------------------')
        print('-1. Aceptar Solicitud                          -')
        print('-2. Ver Cola                                   -')
        print('-3. Ver Lista Circular                         -')
        print('-4. Cerrar Sesión                              -')
        opcion = input('> ')
        if opcion == '1':
            AceptarSolicitud()
        elif opcion == '2':
            colaSolicitudes.graficar()
        elif opcion == '3':
            artista = listaArtistas.obtenerUsuario(id_logueado)
            artista.procesadas.graficar()
        elif opcion == '4':
            id_logueado = None
            break

def AceptarSolicitud():
    global id_logueado
    solicitud = colaSolicitudes.verPrimero()
    if solicitud == None:
        return
    #LO SACAMOS DE LA COLA
    solicitud_aceptada = colaSolicitudes.dequeue()
    #INSERTAN EN LA LISTA CIRCULAR
    listaArtistas.insertarProcesados(id_logueado,solicitud_aceptada)
    #GENERAMOS LA FIGURA
    matriz_figura = MatrizDispersa()
    #PARSEAR EL XML
    tree = ET.parse(solicitud_aceptada.ruta_xml)
    #Obtengo el elemento raiz
    root = tree.getroot()
    nombre_figura = ''
    for elemento in root:
        if elemento.tag == 'diseño':
            for pixel in elemento:
                fila = int(pixel.attrib['fila'])
                columna = int(pixel.attrib['col'])
                color = pixel.text
                matriz_figura.insertar(fila,columna,color)
        elif elemento.tag == 'nombre':
            nombre_figura = elemento.text

    
    #GRAFICAMOS
    ruta = matriz_figura.graficar(solicitud_aceptada.id)
    #creamos el nuevo objeto imagen para insertarlo a la lista doble del usuario
    nueva_imagen = Imagen(solicitud_aceptada.id,nombre_figura,ruta)
    #insertamos el objeto a la lista doble del usuario
    listaSolicitantes.insertarImagenUsuario(solicitud_aceptada.id_solicitante,nueva_imagen)




def MenuSolicitante():
    global id_logueado
    print(id_logueado)
    solicitante:Solicitante = listaSolicitantes.buscar(id_logueado)
    imagen = None
    print(len(solicitante.imagenes))
    if len(solicitante.imagenes) != 0:
        imagen:Imagen = solicitante.imagenes.primero.valor
    while True:
        print('--------------GALERIA--------------')
        if imagen == None:
            print('---------------NO HAY IMAGENES------------')
        else:
            ImagenActual(imagen)
        print('')
        print('-----------------OPCIONES-----------------------')
        print('-1. Ver Anterior                               -')
        print('-2. Ver Siguiente                              -')
        print('-3. Cargar XML                                 -')
        print('-4. Solicitar                                  -')
        print('-5. Ver Pila                                   -')
        print('-6. Ver Lista Doble                            -')
        print('-7. Salir                                      -')
        opcion = input('> ')
        if opcion == '1':
            imagen = solicitante.imagenes.obtenerAnterior()
        elif opcion == '2':
            imagen = solicitante.imagenes.obtenerSiguiente()
        elif opcion == '3':
            CargarXMLFiguras()
        elif opcion == '4':
            Solicitar()
        elif opcion == '5':
            solicitante.pila.graficar()
        elif opcion == '6':
            solicitante.imagenes.graficar()
        elif opcion == '7':
            id_logueado = None
            break

def ImagenActual(imagen):
    print(f'Nombre: {imagen.nombre}')
    print(f'Ruta Imagen: {imagen.ruta_imagen}')
    print(f'ID: {imagen.id}')

def CargarXMLFiguras():
    global id_logueado
    ruta = filedialog.askopenfilename(title="Cargar Archivo", filetypes=(('Text files', '*.xml'), ('All files','*.*')))
    #PARSEAR EL XML
    tree = ET.parse(ruta)
    #Obtengo el elemento raiz
    root = tree.getroot()

    id = ''
    if root.tag == "figura":
        for elementos in root:
            if elementos.tag == "nombre":
                id = elementos.attrib["id"]
    
    nueva = SolicitudPila(id,ruta)
    listaSolicitantes.insertaraPilaUsuario(id_logueado,nueva)

def Solicitar():
    global id_logueado
    valorSacado = listaSolicitantes.sacardePilaUsuario(id_logueado)
    while valorSacado != None:
        nueva_solicitud = SolicitudCola(valorSacado.id,valorSacado.ruta_xml,id_logueado)
        colaSolicitudes.enqueue(nueva_solicitud)
        valorSacado = listaSolicitantes.sacardePilaUsuario(id_logueado)

if __name__ == "__main__":
    inicio()