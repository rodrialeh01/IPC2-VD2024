import os
from xml.etree import ElementTree as ET

from flask import Blueprint, jsonify, request
from models.Usuario import Usuario

#crear un blueprint
BlueprintUsuario = Blueprint('usuarios', __name__)

#RUTA: http://localhost:4000/usuarios/carga
@BlueprintUsuario.route('/usuarios/carga', methods=['POST'])
def cargarUsuarios():

    lista_usuarios = preCargarXML()

    try:
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'message': 'Error al cargar los usuarios: EL XML está vacio',
                'status': 404
            }), 404

        root = ET.fromstring(xml_entrada)

        for usuario in root:
            id = usuario.attrib['id']
            if validarRepetido(id, lista_usuarios):
                continue
            pwd = usuario.attrib['pwd']
            nombre = ''
            correo = ''
            telefono = ''
            direccion = ''
            perfil = ''
            for hijos in usuario:
                if hijos.tag == 'NombreCompleto':
                    nombre = hijos.text
                elif hijos.tag == 'CorreoElectronico':
                    correo = hijos.text
                elif hijos.tag == 'NumeroTelefono':
                    telefono = hijos.text
                elif hijos.tag == 'Direccion':
                    direccion = hijos.text
                elif hijos.tag == 'perfil':
                    perfil = hijos.text

            nuevo_usuario = Usuario(id,pwd,nombre,correo,telefono,direccion, perfil)
            lista_usuarios.append(nuevo_usuario)
        crearXML(lista_usuarios)
        return jsonify({
            'mensaje':'Usuarios cargados con éxito',
            'status':201
        }),201

    except:
        return jsonify({
            'message': 'Error al cargar los usuarios',
            'status': 404
        }), 404
    
#RUTA: http://localhost:4000/usuarios/json
@BlueprintUsuario.route('/usuarios/json', methods=['GET'])
def getUsuariosJSON():
    lista_usuarios = preCargarXML()
    usuarios = []
    for usuario in lista_usuarios:
        user = {
            'id': usuario.id,
            'nombre': usuario.nombre,
            'correo': usuario.correo,
            'telefono': usuario.telefono,
            'direccion': usuario.direccion,
            'perfil': usuario.perfil
        }
        usuarios.append(user)
    
    return jsonify({
        'usuarios': usuarios,
        'status': 200
    }),200

#RUTA: http://localhost:4000/usuarios/xml
@BlueprintUsuario.route('/usuarios/xml', methods=['GET'])
def getUsuariosXML():
    lista_usuarios = preCargarXML()
    tree = ET.Element('usuarios')
    for usuario in lista_usuarios:
        #2. Creamos un elemento usuario
        usuario_xml = ET.SubElement(tree, 'usuario', id=usuario.id, pwd=usuario.password)
        #3. Creamos los elementos hijos
        nombre = ET.SubElement(usuario_xml, 'NombreCompleto')
        nombre.text = usuario.nombre
        correo = ET.SubElement(usuario_xml, 'CorreoElectronico')
        correo.text = usuario.correo
        telefono = ET.SubElement(usuario_xml, 'NumeroTelefono')
        telefono.text = usuario.telefono
        direccion = ET.SubElement(usuario_xml, 'Direccion')
        direccion.text = usuario.direccion
        perfil = ET.SubElement(usuario_xml, 'perfil')
        perfil.text = usuario.perfil
        imagenes = ET.SubElement(usuario_xml, 'imagenes')
    
    ET.indent(tree, space='\t', level=0)
    xml_str = ET.tostring(tree, encoding='utf-8', xml_declaration=True)
    return xml_str

#RUTA: http://localhost:4000/usuarios/login
@BlueprintUsuario.route('/usuarios/login', methods=['POST'])
def login():
    '''
    JSON DE ENTRADA
    {
        'id': id del usuario,
        'password': contraseña del usuario
    }
    '''

    lista_usuarios = preCargarXML()

    id = request.json['id']
    password = request.json['password']

    if id == 'admin' and password == 'admin':
        return jsonify({
            'message':'Bienvenido admin',
            'rol':1,
            'accion': True,
            'status': 200
        })

    for usuario in lista_usuarios:
        if usuario.id == id and usuario.password == password:
            return jsonify({
                'message': 'Bienvenido '+usuario.nombre,
                'rol':2,
                'accion': True,
                'status': 200
                }),200
    
    return jsonify({
        'message': 'Credenciales invalidas',
        'rol':0,
        'accion': False,
        'status': 200
        }),200



def validarRepetido(id, lista_usuarios):
    for usuario in lista_usuarios:
        if usuario.id == id:
            return True
    return False

'''
PERSISTENCIA
    XML PARA PERSISTENCIA DE DATOS: database/usuarios.xml
    1. CREAR XML: CADA VEZ QUE SE EDITE, O SE AGREGUE UN NUEVO DATO LLAMAMOS A ESTA FUNCION
    2. PRE-CARGAR XML: CARGA EL XML DE LA DATABABASE Y LO GUARDA EN UNA LISTA
'''

def crearXML(usuarios):
    #Si existe el archivo, se elimina
    if os.path.exists('/database/usuarios.xml'):
        os.remove('/database/usuarios.xml')
    
    #CREAMOS EL XML
    #1. Creamos el elemento raiz
    tree = ET.Element('usuarios')
    for usuario in usuarios:
        #2. Creamos un elemento usuario
        usuario_xml = ET.SubElement(tree, 'usuario', id=usuario.id, pwd=usuario.password)
        #3. Creamos los elementos hijos
        nombre = ET.SubElement(usuario_xml, 'NombreCompleto')
        nombre.text = usuario.nombre
        correo = ET.SubElement(usuario_xml, 'CorreoElectronico')
        correo.text = usuario.correo
        telefono = ET.SubElement(usuario_xml, 'NumeroTelefono')
        telefono.text = usuario.telefono
        direccion = ET.SubElement(usuario_xml, 'Direccion')
        direccion.text = usuario.direccion
        perfil = ET.SubElement(usuario_xml, 'perfil')
        perfil.text = usuario.perfil
    
    #4. Creamos el arbol
    tree = ET.ElementTree(tree)
    #5. Agregamos formato de identacion
    ET.indent(tree, space='\t', level=0)
    #6. Escribimos el arbol en el archivo xml
    tree.write('database/usuarios.xml', encoding='utf-8', xml_declaration=True)

def preCargarXML():
    #Si no existe el archivo, retorna una lista vacia
    if not os.path.exists('database/usuarios.xml'):
        return []
    
    #creamos una lista de usuarios
    usuarios = []

    tree = ET.parse('database/usuarios.xml')
    root = tree.getroot()
    for usuario in root:
        id = usuario.attrib['id']
        pwd = usuario.attrib['pwd']
        nombre = ''
        correo = ''
        telefono = ''
        direccion = ''
        perfil = ''
        for hijo in usuario:
            if hijo.tag == 'NombreCompleto':
                nombre = hijo.text
            elif hijo.tag == 'CorreoElectronico':
                correo = hijo.text
            elif hijo.tag == 'NumeroTelefono':
                telefono = hijo.text
            elif hijo.tag == 'Direccion':
                direccion = hijo.text
            elif hijo.tag == 'perfil':
                perfil = hijo.text
        
        #creamos un objeto usuario
        nuevo_usuario = Usuario(id,pwd,nombre, correo, telefono, direccion, perfil)
        usuarios.append(nuevo_usuario)
    
    return usuarios
