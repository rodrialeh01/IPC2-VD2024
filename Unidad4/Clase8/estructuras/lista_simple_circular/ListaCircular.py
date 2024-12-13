import os

from estructuras.lista_simple_circular.nodo import Nodo


class ListaCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    def __len__(self):
        return self.tamanio
    
    def insertar(self, valor):
        nuevo = Nodo(valor)
        # SI LA LISTA ESTA VACIA
        if self.primero == None and self.ultimo == None:
            #1. Asignamos el nuevo nodo al primero de la lista
            self.primero = nuevo
            #2. Asignamos el nuevo nodo al ultimo de la lista
            self.ultimo = nuevo
            #3. El ultimo nodo apunta al primer nodo
            self.ultimo.siguiente = self.primero
        # SI LA LISTA NO ESTA VACIA
        else:
            #1. El siguiente del ultimo nodo apunta al nuevo nodo
            self.ultimo.siguiente = nuevo
            #2. El ultimo nodo va a ser ahora el nuevo nodo
            self.ultimo = nuevo
            #3. El siguiente del ultimo nodo va a apuntar al primer nodo
            self.ultimo.siguiente = self.primero
        self.tamanio+=1

    def mostrar(self):
        contador = 0
        actual = self.primero
        while contador < self.tamanio:
            print(actual.valor)
            actual = actual.siguiente
            contador+=1
    
    def obtenerValor(self, id):
        contador = 0
        actual = self.primero
        while contador < self.tamanio:
            if actual.valor.id == id:
                return actual.valor
            actual = actual.siguiente
            contador+=1
        return None

    def graficar(self):
        codigo_dot = ''

        #CREAMOS EL CODIGO PARA LA LISTA
        codigo_dot += '''digraph G {
    rankdir=LR;
    node[shape=record, height=.1]
'''
        #CREAMOS LOS NODOS
        contador_nodos = 0
        actual = self.primero
        while contador_nodos < self.tamanio:
            codigo_dot += 'nodo'+str(contador_nodos)+'[label=\"{'+str(actual.valor)+'|<f1>}\"];\n'
            actual = actual.siguiente
            contador_nodos+=1
        
        #CREAMOS LOS ENLACES
        actual = self.primero
        contador_nodos = 0
        while contador_nodos < self.tamanio-1:
            codigo_dot += 'nodo'+str(contador_nodos)+' -> nodo'+str(contador_nodos+1)+';\n'
            actual = actual.siguiente
            contador_nodos+=1
        
        #AGREGAMOS EL ULTIMO ENLACE
        codigo_dot += 'nodo'+str(self.tamanio-1)+ ' -> nodo0[constraint=false];\n'

        codigo_dot += '}'

        #CREAMOS EL ARCHIVO DOT
        ruta_dot = 'reportesdot/listaCircular.dot'
        archivo = open(ruta_dot, 'w')
        archivo.write(codigo_dot)
        archivo.close()

        #GENERAR LA IMAGEN
        ruta_imagen = 'reportes/listaCircular.pdf'
        comando = 'dot -Tpdf '+ruta_dot + ' -o '+ruta_imagen
        os.system(comando)

        #ABRIMOS LA IMAGEN
        ruta_abrir_imagen = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_imagen)