from xml.etree import ElementTree as ET

from clases.usuario import Usuario
from estructuras.estructuras import lista_usuarios
from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

#Creamos nuestra Aplicacion
app = Flask(__name__)

#Le damos permisos de CORS
cors = CORS(app)

#DESDE AQUI CREAMOS NUESTROS ENDPOINTS
@app.route('/', methods=['GET'])
def inicio():
    return '<h1>Bienvenido a mi API de la clase 13 de IPC2 VD2024</h1><br/><p>Hola desde python</p>'

#1. CREATE = POST
#RUTA: http://localhost:4000/usuario/crear
@app.route('/usuario/crear', methods=['POST'])
def crear_usuario():
    #Recibimos los datos del usuario
    '''
    JSON DE ENTRADA
    {
        'id': id del usuario
        'nombre': nombre del usuario
        'password': contraseña del usuario
    }
    '''
    try:
        #VAMOS A LEER LOS DATOS QUE VIENEN DEL JSON
        #request.json[nombre de la clave del json]
        id = request.json['id']
        nombre = request.json['nombre']
        password = request.json['password']
        #CREAMOS UN NUEVO OBJETO USUARIO
        nuevo_usuario = Usuario(id,nombre,password)
        #AGREGAMOS EL NUEVO USUARIO A LA LISTA DE USUARIOS
        lista_usuarios.append(nuevo_usuario)
        return jsonify({
            'mensaje': 'Usuario creado con exito',
            'status': 201
        }),201
    except:
        return jsonify({
            'mensaje': 'Hubo un error',
            'status': 500
        }),500

#2. READ = GET
#RUTA: http://localhost:4000/usuario/lista
@app.route('/usuario/lista', methods=['GET'])
def verListaUsuarios():
    usuarios = []
    for usuario in lista_usuarios:
        diccionario_usuario = {
            'id': usuario.id,
            'nombre': usuario.nombre
        }
        usuarios.append(diccionario_usuario)
    return jsonify({
        'usuarios': usuarios,
        'status': 200
    }),200

#3. UPDATE = PUT / PATCH
'''
PUT:
    SIRVE PARA CAMBIOS TOTALES DE UN OBJETO
PATCH:
    SIRVE PARA CAMBIOS PARCIALES DE UN OBJETO
'''
#RUTA: http://localhost:4000/usuario/editar/:id
@app.route('/usuario/editar/<string:id>', methods=['PUT'])
def editarUsuarioPUT(id):
    try:
        #VAMOS A LEER LOS DATOS QUE VIENEN DEL JSON
        '''
        JSON DE ENTRADA
        {
            'nombre': nombre del usuario
            'password': contraseña del usuario
        }
        Y LOS PARAMETROS SON
        /id
        '''
        #request.json[nombre de la clave del json]
        nombre = request.json['nombre']
        password = request.json['password']
        #BUSCAMOS LA COINCIDENCIA CON EL ID
        for usuario in lista_usuarios:
            if usuario.id == id:
                #CAMBIAMOS LOS DATOS DEL USUARIO
                usuario.nombre = nombre
                usuario.password = password
                return jsonify({
                    'mensaje': 'Usuario editado con exito',
                    'status': 200
                }),200
        
        #SI NO ENCUENTRA EL USUARIO
        return jsonify({
            'mensaje': 'No se encontro el usuario',
            'status': 404
            }),404
    except:
        return jsonify({
            'mensaje': 'Hubo un error',
            'status': 500
            }),500

#RUTA: http://localhost:4000/usuario/editarnombre/:id
@app.route('/usuario/editarnombre/<string:id>', methods=['PATCH'])
def editarNombreUsuario(id):
    try:
        #VAMOS A LEER LOS DATOS QUE VIENEN DEL JSON
        '''
        JSON DE ENTRADA
        {
            'nombre': nombre del usuario
        }
        Y LOS PARAMETROS SON
        /id
        '''

        nombre = request.json['nombre']
        #BUSCAMOS LA COINCIDENCIA CON EL ID
        for usuario in lista_usuarios:
            if usuario.id == id:
                #CAMBIAMOS LOS DATOS DEL USUARIO
                usuario.nombre = nombre
                return jsonify({
                    'mensaje': 'Usuario editado con exito',
                    'status': 200
                    }),200
        
        #SI NO ENCUENTRA EL USUARIO
        return jsonify({
            'mensaje': 'No se encontro el usuario',
            'status': 404
            }),404
    except:
        return jsonify({
            'mensaje': 'Hubo un error',
            'status': 500
            }),500

#4. DELETE = DELETE
#RUTA: http://localhost:4000/usuario/eliminar/:id
@app.route('/usuario/eliminar/<string:id>', methods=['DELETE'])
def eliminarUsuario(id):
    #ELIMINACIÓN FISICA
    for usuario in lista_usuarios:
        if usuario.id == id:
            lista_usuarios.remove(usuario)
            return jsonify({
                'mensaje': 'Usuario eliminado con exito',
                'status': 200
                }),200
    
    return jsonify({
        'mensaje': 'No se encontro el usuario',
        'status': 404
        }),404

#RUTA: http://localhost:4000/usuario/xml
@app.route('/usuario/xml', methods=['POST'])
def leerXMLUsuario():
    try:
        #OBTENER EL XML
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'mensaje': 'No se recibio el xml',
                'status': 400
                }),400
        #LEEMOS EL XML
        root = ET.fromstring(xml_entrada)
        #OBTENER LOS DATOS DEL USUARIO
        id = ''
        nombre = ''
        password = ''
        for datos in root:
            if datos.tag == 'id':
                id = datos.text
            elif datos.tag == 'nombre':
                nombre = datos.text
            elif datos.tag == 'password':
                password = datos.text
        
        #VALIDAR LOS DATOS
        if id == '' or nombre == '' or password == '':
            return jsonify({
                'mensaje': 'Faltan datos',
                'status': 400
            }),400
        #CREAMOS EL OBJETO
        nuevo_usuario = Usuario(id,nombre,password)
        #EL OBJETO SE AÑADE A LA LISTA DE USUARIOS
        lista_usuarios.append(nuevo_usuario)
        #CREAMOS UN DICCIONARIO PARA MOSTRAR EL JSON DE DATOS DE XML
        usuario_diccionario = {
            'id': nuevo_usuario.id,
            'nombre': nuevo_usuario.nombre,
            'password': nuevo_usuario.password
        }
        return jsonify({
            'mensaje': 'Usuario creado con exito',
            'usuario': usuario_diccionario,
            'status': 200
        }),200

    except:
        return jsonify({
            'mensaje': 'Hubo un error',
            'status': 500
            }),500

'''
SI UNA RUTA TIENE MÁS DE 1 MÉTODO HTTP

FORMA 1:
@app.route('/usuario/<string:id>', methods=['GET', 'DELETE'])
def acciones_usuario(id):
    if request.method == 'GET':
        pass
    elif request.method == 'DELETE':
        pass

FORMA 2:
@app.route('/usuario', method=['GET'])
def get_usuario():
    if request.method == 'GET':
        pass

@app.route('/usuario', method=['DELETE'])
def eliminar_usuario():
    if request.method == 'DELETE':
        pass
'''
#LLAMAMOS LA EJECUCIÓN DE LA API EN LA MAIN
if __name__ == "__main__":
    #app.run(host=LOCALHOST, port=PUERTO A HABILITAR PARA MI API, debug=True si quiero que se reinicie automaticamente)
    app.run(host="0.0.0.0", port=4000, debug=True)