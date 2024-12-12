import os

from estructuras.lista_simple.nodo import Nodo


class ListaSimple:
    def __init__(self):
        self.primero = None
        self.tamanio = 0
    
    #len(lista)
    def __len__(self):
        return self.tamanio
    
    # INSERTAR -> AL FINAL DE LA LISTA
    def insertar(self, valor):

        #VALIDAR QUE YA EXISTE UN USUARIO
        if self.validarExiste(valor.id) == True:
            return

        # CREAR EL NODO
        nuevo = Nodo(valor)
        # VERIFICAMOS SI LA LISTA ESTA VACIA
        if self.primero == None:
            self.primero = nuevo
        # SI LA LISTA NO ESTA VACIA
        else:
            actual = self.primero
            while actual != None:
                if actual.siguiente == None:
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente
        self.tamanio+=1

    def imprimirLista(self):
        actual = self.primero
        while actual != None:
            print(str(actual.valor))
            actual = actual.siguiente
    
    def obtenerUsuario(self,id):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                return actual.valor
            actual = actual.siguiente
        return None

    def loginUsuario(self, id, pwd):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id and actual.valor.password == pwd:
                return True
            actual = actual.siguiente
        return False

    def validarExiste(self,id):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                return True
            actual = actual.siguiente
        return False
    
    def graficar(self):
        codigodot = ''
        codigodot += '''digraph G {
    rankdir=LR;
    node[shape=record, height=.1]
    '''
        contador_nodos = 1

        #CREAR LOS NODOS
        actual = self.primero
        while actual != None:
            codigodot += 'nodo'+str(contador_nodos)+'[label=\"{'+str(actual.valor)+'|<f1>}\"];\n'
            contador_nodos+=1
            actual = actual.siguiente
        
        #CREAR LOS ENLACES
        actual = self.primero
        contador_nodos = 1
        while actual.siguiente != None:
            codigodot += 'nodo'+str(contador_nodos)+' -> nodo'+str(contador_nodos+1)+';\n'
            contador_nodos+=1
            actual = actual.siguiente
        
        codigodot += '}'

        #ESCRIBIR EL TEXTO CONCATENASO AL ARCHIVO DOT

        #defino la ruta donde se guarda el codigo dot
        ruta_dot = 'reportesdot/listaSimple.dot'
        #creamos el archivo dot
        archivo = open(ruta_dot,'w')
        #escribimos el archivo
        archivo.write(codigodot)
        #cerramos el archivo
        archivo.close()

        # GENERACIÓN DE LA IMAGEN
        
        #defino la ruta donde se guarda la imagen
        ruta_imagen = 'reportes/listaSimple.png'
        #defino el comando de graphviz para compilar el dot y generar la imagen
        comando = 'dot -Tpng '+ ruta_dot + ' -o ' + ruta_imagen
        #ejecuto el comando
        os.system(comando)

        # ABRIR LA IMAGEN

        #1. CONVERTIMOS LA RUTA RELATIVA A UNA RUTA ABSOLUTA
        # RUTA RELATIVA: ./hola.txt
        # RUTA ABSOLUTA: C://users/equis/documents/hola.txt
        ruta_abrir_imagen = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_imagen)
        print('grafico generado con exito')
    
    def insertarProcesados(self,id,procesado):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                actual.valor.procesadas.insertar(procesado)
                break
            actual = actual.siguiente
