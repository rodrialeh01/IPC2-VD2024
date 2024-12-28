import os
from xml.etree import ElementTree as ET

from flask import Blueprint, jsonify, request
from models.Imagen import Imagen
from models.matrizDispersa.matrizDispersa import MatrizDispersa
from models.Pixel import Pixel

#creamos un blueprint
BlueprintImagen = Blueprint('imagenes', __name__)

#RUTA: http://localhost:4000/imagenes/carga/:id_usuario
@BlueprintImagen.route('/imagenes/carga/<string:id_usuario>', methods=['POST'])
def cargaImagen(id_usuario):
    
    lista_imagenes = preCargarXMLImagenes()

    try:
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'mensaje': 'No se recibió el archivo XML',
                'status': 400
            }), 400

        root = ET.fromstring(xml_entrada)
        #crear la matriz
        matriz = MatrizDispersa()
        nombre = ''
        pixeles = []
        id = len(lista_imagenes) + 1
        for hijo in root:
            if hijo.tag == 'nombre':
                nombre = hijo.text
            elif hijo.tag == 'diseño':
                for pixel in hijo:
                    fila = int(pixel.attrib['fila'])
                    columna = int(pixel.attrib['col'])
                    color = pixel.text
                    #1. lo insertamos en nuestra matriz
                    matriz.insertar(fila,columna,color)
                    #2. Creamos el objeto pixel
                    nuevo_pixel = Pixel(fila,columna,color)
                    pixeles.append(nuevo_pixel)
        
        #3. Creamos el objeto imagen
        nueva_imagen = Imagen(id, id_usuario, nombre, pixeles)
        lista_imagenes.append(nueva_imagen)
        crearXML(lista_imagenes)
        return jsonify({
            'mensaje': 'Imagen cargada correctamente',
            'matriz': matriz.graficar(),
            'status': 200
            }), 200
    
    except:
        return jsonify({
            'message': 'Error al cargar la imagen',
            'status': 404
        }), 404
    
#RUTA: http://localhost:4000/imagenes/editar/:id_usuario
@BlueprintImagen.route('/imagenes/editar/<string:id_usuario>', methods=['POST'])
def editarImagen(id_usuario):
    lista_imagenes = preCargarXMLImagenes()

    '''
    JSON DE ENTRADA
    {
        'id': id de la imagen,
        'filtro': 1 para escala de grises/2 para tonalidad sepia
    }
    '''

    id = int(request.json['id'])
    filtro = int(request.json['filtro'])
    imagenActual:Imagen = None

    for imagen in lista_imagenes:
        if imagen.id == id:
            imagenActual = imagen
            break

    if imagenActual is None:
        return jsonify({
            'mensaje':'Imagen no encontrada',
            'status':404
            }),404
    
    #1. Creamos una lista de nuevos pixeles para crear la nueva imagen
    nuevos_pixeles = []
    #Matriz1: Matriz original
    matriz1 = MatrizDispersa()
    #Matriz2: Matriz Editada
    matriz2 = MatrizDispersa()

    #Recorro la imagen original para insertarlo a la matriz dispersa 1
    for pixel in imagenActual.pixeles:
        pixel:Pixel
        #Insertamos los pixeles a la matriz1
        matriz1.insertar(pixel.fila, pixel.columna, pixel.color)

        #Aplicamos filtros
        #1. Escala de grises
        if filtro == 1:
            #1. Pasamos de hexadecimal a RGB
            rgb_pixel = HexToRGB(pixel.color)
            #2. Pasamos el RGB a escala de grises
            rgb_escala_grises = rgbToGrayScale(rgb_pixel)
            #3. Pasamos el escala de grises a hexadecimal
            nuevo_color = rgbToHex(rgb_escala_grises)
            #4. Insertamos el nuevo pixel a la matriz2
            matriz2.insertar(pixel.fila, pixel.columna, nuevo_color)
            #5. Creamos un nuevo pixel
            nuevo_pixel = Pixel(pixel.fila, pixel.columna, nuevo_color)
            nuevos_pixeles.append(nuevo_pixel)
        #2. Tonalidad sepia
        elif filtro == 2:
            #1. Pasamos de hexadecimal a RGB
            rgb_pixel = HexToRGB(pixel.color)
            #2. Pasamos el RGB a sepia
            rgb_sepia = rgbToSepia(rgb_pixel)
            #3. Pasamos la tonalidad sepia a hexadecimal
            nuevo_color = rgbToHex(rgb_sepia)
            #4. Insertamos el nuevo pixel a la matriz2
            matriz2.insertar(pixel.fila, pixel.columna, nuevo_color)
            #5. Creamos un nuevo pixel
            nuevo_pixel = Pixel(pixel.fila, pixel.columna, nuevo_color)
            nuevos_pixeles.append(nuevo_pixel)
    
    id = len(lista_imagenes) + 1
    #2. Creamos una nueva imagen con los pixeles nuevos
    nueva_imagen = Imagen(id,id_usuario, imagenActual.nombre, nuevos_pixeles)
    nueva_imagen.editado = True
    lista_imagenes.append(nueva_imagen)
    crearXML(lista_imagenes)

    return jsonify({
        'mensaje': 'Imagen editada correctamente',
        'matriz1': matriz1.graficar(),
        'matriz2': matriz2.graficar(),
        'status': 201
    }), 201

def HexToRGB(hex_color):
    """
    Convierte un color en formato hexadecimal (#RRGGBB) a formato RGB.

    Args:
        hex_color (str): Color en formato hexadecimal (por ejemplo, '#FFFFFF').

    Returns:
        tuple: Una tupla con los valores RGB (rojo, verde, azul).
    """

    #Eliminamos el simbolo '#'
    hex_color = hex_color.lstrip('#')

    #convertimos el string hexadecimal a valores RGB
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    return (red, green, blue)

def rgbToGrayScale(rgb_color):
    """
    Convierte un color RGB a su equivalente en escala de grises (en formato RGB).

    Args:
        rgb_color (tuple): Una tupla con los valores RGB (rojo, verde, azul).

    Returns:
        tuple: Una tupla con los valores RGB en escala de grises.
    """

    red, green, blue = rgb_color

    #Obtenemos el nuevo gris
    gris = 0.2989*red + 0.5870*green + 0.1140*blue

    gris = round(gris)

    return (gris, gris, gris)

def rgbToSepia(rgb_color):
    """
    Convierte un color RGB a su equivalente en tonalidad sepia (en formato RGB).

    Args:
        rgb_color (tuple): Una tupla con los valores RGB (rojo, verde, azul).

    Returns:
        tuple: Una tupla con los valores RGB en tonalidad sepia.
    """

    red,green, blue = rgb_color

    #calculamos los nuevos colores
    new_red = 0.393*red + 0.769*green + 0.189*blue
    new_green = 0.349*red + 0.686*green + 0.168*blue
    new_blue = 0.272*red + 0.534*green + 0.131*blue

    new_red = round(new_red)
    new_green = round(new_green)
    new_blue = round(new_blue)

    return (new_red, new_green, new_blue)

def rgbToHex(rgb_color):
    """
    Convierte un color en formato RGB a un string en formato hexadecimal.

    Args:
        rgb_color (tuple): Una tupla con los valores RGB (rojo, verde, azul).

    Returns:
        str: El color en formato hexadecimal (por ejemplo, '#RRGGBB').
    """

    return "#{:02X}{:02X}{:02X}".format(rgb_color[0], rgb_color[1], rgb_color[2])

def crearXML(imagenes):
    #si existe el archivo, se elimina
    if os.path.exists('database/imagenes.xml'):
        os.remove('database/imagenes.xml')
    
    #CREAR EL XML
    tree = ET.Element('imagenes')
    for imagen in imagenes:
        imagen:Imagen
        editado = 0
        if imagen.editado == True:
            editado = 1
        imagen_xml = ET.SubElement(tree, 'imagen', id=str(imagen.id), id_usuario=str(imagen.id_usuario), editado=str(editado))
        nombre_xml = ET.SubElement(imagen_xml, 'nombre')
        nombre_xml.text = imagen.nombre
        diseño_xml = ET.SubElement(imagen_xml, 'diseño')
        for pixel in imagen.pixeles:
            pixel:Pixel
            pixel_xml = ET.SubElement(diseño_xml, 'pixel', fila=str(pixel.fila), col=str(pixel.columna))
            pixel_xml.text = pixel.color
    
    tree = ET.ElementTree(tree)

    ET.indent(tree, space='\t', level=0)

    tree.write('database/imagenes.xml', encoding='utf-8', xml_declaration=True)

def preCargarXMLImagenes():
    if not os.path.exists('database/imagenes.xml'):
        return []
    
    #creamos una lista de imagenes
    imagenes = []

    tree = ET.parse('database/imagenes.xml')
    root = tree.getroot()
    for imagen in root:
        id = int(imagen.attrib['id'])
        id_usuario = imagen.attrib['id_usuario']
        editado = imagen.attrib['editado']
        if editado == '1':
            editado = True
        elif editado == '0':
            editado = False
        nombre = ''
        pixeles = []
        for hijo in imagen:
            if hijo.tag == 'nombre':
                nombre = hijo.text
            elif hijo.tag == 'diseño':
                for pixel in hijo:
                    fila = int(pixel.attrib['fila'])
                    columna = int(pixel.attrib['col'])
                    color = pixel.text
                    nuevo_pixel = Pixel(fila,columna,color)
                    pixeles.append(nuevo_pixel)
        
        nueva_imagen = Imagen(id,id_usuario, nombre, pixeles)
        nueva_imagen.editado = editado
        imagenes.append(nueva_imagen)
    
    return imagenes