import os

from estructuras.lista_doble.nodo import Nodo


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    
    def __len__(self):
        return self.tamanio

    #INSERCION AL FINAL DE LA LISTA
    def insertar(self, valor):
        #CREAMOS EL NODO
        nuevo = Nodo(valor)
        #VERIFICAMOS SI LA LISTA ESTA VACIA
        if self.primero == None and self.ultimo == None:
            self.primero = nuevo
            self.ultimo = nuevo
        # SI LA LISTA NO ESTA VACIA
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo
        #AUMENTAMOS EL CONTADOR DE TAMAÑO DE LA LISTA
        self.tamanio += 1
    
    def imprimirListaHaciaAdelante(self):
        actual = self.primero
        while actual != None:
            print(str(actual.valor))
            actual = actual.siguiente
    
    def imprimirListaHaciaAtras(self):
        actual = self.ultimo
        while actual != None:
            print(str(actual.valor))
            actual = actual.anterior
    
    def buscar(self, id):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                return actual.valor
            actual = actual.siguiente
        return None
    
    def login(self, id,pwd):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id and actual.valor.password == pwd:
                return True
            actual = actual.siguiente
        return False
    
    def graficar(self):
        codigo_dot = ''
        codigo_dot += '''digraph G {
    rankdir=LR;
    node[shape=record, height=.1]
    '''
        
        #CREAMOS LOS NODOS
        actual = self.primero
        contador_nodos = 1

        while actual != None:
            codigo_dot += 'nodo'+str(contador_nodos)+'[label=\"{<f1>|'+str(actual.valor)+'|<f2>}\"];\n'
            contador_nodos+=1
            actual = actual.siguiente
        
        #CREAMOS LOS ENLACES
        actual = self.primero
        contador_nodos = 1
        while actual.siguiente != None:
            #RELACION DE IZQUIERDA A DERECHA
            codigo_dot += 'nodo'+str(contador_nodos)+':f2 -> nodo'+str(contador_nodos+1)+':f1;\n'
            #RELACION DE DERECHA A IZQUIERDA
            codigo_dot += 'nodo'+str(contador_nodos+1)+':f1 -> nodo'+str(contador_nodos)+':f2;\n'
            contador_nodos+=1
            actual = actual.siguiente
        
        codigo_dot += '}'

        #CREAMOS Y ESCRIBIMOS EL ARCHIVO .DOT
        ruta_dot = 'reportesdot/listaDoble.dot'

        #creo el archivo
        archivo = open(ruta_dot, 'w')
        archivo.write(codigo_dot)
        archivo.close()

        #generamos la imagen
        ruta_imagen = 'reportes/listaDoble.svg'
        comando = 'dot -Tsvg ' + ruta_dot + ' -o ' + ruta_imagen
        os.system(comando)

        #CONVIERTO LA RUTA RELATIVA A RUTA ABSOLUTA
        ruta_abrir_imagen = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_imagen)
        print('Se genero la grafica de la lista doblemente enlazada')

    def insertaraPilaUsuario(self,id, valor):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                actual.valor.pushPila(valor)
                break
            actual = actual.siguiente
    
    def sacardePilaUsuario(self,id):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                if actual.valor.pila.isEmpty():
                    return None
                else:
                    return actual.valor.popPila()
            actual = actual.siguiente
    
    def insertarImagenUsuario(self,id,imagen):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id:
                print('si xd')
                actual.valor.insertarImagen(imagen)
                break
            actual = actual.siguiente
        print('no :v')
