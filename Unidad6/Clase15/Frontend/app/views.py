import json

import requests
#para el cache
from django.core.cache import cache
#para las cookies
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import FileForm, LoginForm

# Create your views here.

endpoint = 'http://localhost:4000/'

contexto = {
    'contenido_archivo': None,
    'binario_xml':None
}

#Esta es una vista de ejemplo, pero puedes agregar las que necesites
def index(request):
    return render(request, 'index.html')

def loginPage(request):
    return render(request, 'login.html')

def iniciarSesion(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                #Obtenemos losa datos del formulario
                iduser = form.cleaned_data['iduser']
                password = form.cleaned_data['password']

                #PETICION AL BACK
                #ENDPOINT + URL
                url = endpoint + 'usuarios/login'
                #DATA QUE VOY A ENVIAR
                data = {
                    'id': iduser,
                    'password': password
                }

                #convertimos el diccionario data a json
                json_data = json.dumps(data)

                #HEADERS
                headers = {
                    'Content-Type': 'application/json',
                }

                #llamamos a la peticion Backend
                response = requests.post(url, data=json_data, headers=headers)

                respuesta = response.json()

                #obtener el rol
                rol = int(respuesta['rol'])
                usuario_a_loguearse = iduser
                pagina_redireccion = None
                #IR A ADMIN
                if rol == 1:
                    #Si yo quiero almacenar el usuario en cache
                    #cache.set('id_user', usuario_a_loguearse, timeout=None)
                    #Si quiero almacenarlo en la cookies
                    pagina_redireccion = redirect('carga')
                    pagina_redireccion.set_cookie('id_user', iduser)
                    return pagina_redireccion
                elif rol == 2:
                    #Si yo quiero almacenar el usuario en cache
                    #cache.set('id_user', usuario_a_loguearse, timeout=None)
                    #Si quiero almacenarlo en la cookies
                    pagina_redireccion = redirect('user')
                    pagina_redireccion.set_cookie('id_user', iduser)
                    return pagina_redireccion
                else:
                    return render(request, 'login.html')
            
            return render(request, 'login.html')
    except:
        return render(request, 'login.html')
    
def adminPage(request):
    return render(request, 'admin.html')

def cargaAdminPage(request):
    return render(request, 'carga.html')

def cargarXML(request):
    ctx = {
        'contenido': None
    }
    try:
        if request.method == 'POST':
            form = FileForm(request.POST, request.FILES)
            if form.is_valid():
                archivo = request.FILES['file']
                #guardamos el binario
                xml = archivo.read()
                xml_decodificado = xml.decode('utf-8')
                #guardamos el contenido del archivo en nuestro contexto global
                contexto['binario_xml'] = xml
                contexto['contenido_archivo'] = xml_decodificado
                #guardamos el contenido del archivo en nuestro contexto local
                ctx['contenido'] = xml_decodificado
                return render(request, 'carga.html', ctx)
    except:
        return render(request, 'carga.html')

def enviarUsersXML(request):
    try:
        if request.method == 'POST':
            xml = contexto['binario_xml']
            if xml is None:
                return render(request, 'carga.html')
            
            #Peticion al backend
            url = endpoint + 'usuarios/carga'
            response = requests.post(url, data=xml)
            respuesta = response.json()
            print(respuesta)
            contexto['binario_xml'] = None
            contexto['contenido_archivo'] = None
            return render(request, 'carga.html')
    except:
        return render(request, 'carga.html')
    
def verUsuariosPage(request):
    ctx = {
        'usuarios':None
    }
    url = endpoint + 'usuarios/json'
    response = requests.get(url)
    data = response.json()
    ctx['usuarios'] = data['usuarios']
    return render(request, 'users.html', ctx)

def verUsuariosXMLPage(request):
    ctx = {
        'contenido_xml':None
    }
    url = endpoint + 'usuarios/xml'
    response = requests.get(url)
    data = response.text
    ctx['contenido_xml'] = data
    return render(request, 'xmlusers.html', ctx)

def cerrarSesion(request):
    #si estas usando cache
    #cache.delete('id_user')
    #si estas usando cookies
    response = redirect('login')
    response.delete_cookie('id_user')
    return response

def ayuda(request):
    return render(request, 'ayuda.html')

def userPage(request):
    return render(request, 'usuario.html')