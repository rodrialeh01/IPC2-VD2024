import os

from estructuras.lista_doble_circular.nodo import Nodo


class ListaDobleCircular:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    
    def __len__(self):
        return self.tamanio
    
    def insertar(self, valor):
        nuevo = Nodo(valor)
        #SI ESTA VACIA LA LISTA
        if self.primero == None and self.ultimo == None:
            #1. el primero y el ultimo seran el nuevo nodo
            self.primero = nuevo
            self.ultimo = nuevo
            #2. el siguiente del ultimo va a apuntar al primero
            self.ultimo.siguiente = self.primero
            #3. el anterior al primero va a apuntar al ultimo
            self.primero.anterior = self.ultimo
        #SI LA LISTA NO ESTA VACIA
        else:
            #1. El siguiente del ultimo va a apuntar al nuevo nodo
            self.ultimo.siguiente = nuevo
            #2. el anterior del nuevo va a apuntar al que actualmente es el ultimo nodo
            nuevo.anterior = self.ultimo
            #3. el ultimo nodo ahora es el nuevo nodo
            self.ultimo = nuevo
            #4. el siguiente del ultimo nodo va a apuntar al primer nodo
            self.ultimo.siguiente = self.primero
            #5. el anterior al primer nodo va a apuntar al ultimo nodo
            self.primero.anterior = self.ultimo
        self.tamanio+= 1
        print('si inserta')
    
    def mostrar(self):
        contador = 0
        actual = self.primero
        while contador < self.tamanio:
            print(actual.valor)
            actual = actual.siguiente
            contador+= 1
    
    def obtenerSiguiente(self,id):
        actual = self.primero
        contador = 0
        while contador < self.tamanio:
            if actual.valor.id == id:
                return actual.siguiente.valor
            actual = actual.siguiente
            contador+= 1
    
    def obtenerAnterior(self, id):
        actual = self.primero
        contador = 0
        while contador < self.tamanio:
            if actual.valor.id == id:
                return actual.anterior.valor
            actual = actual.siguiente
            contador+= 1
        
    def graficar(self):
        codigodot = ''
        codigodot += '''digraph G {
    rankdir=LR;
    node[shape=record, height=.1]
    '''
        #CREAMOS LOS NODOS
        actual = self.primero
        contador_nodos = 0
        while contador_nodos < self.tamanio:
            codigodot += 'nodo'+str(contador_nodos)+'[label=\"{<f1>|'+str(actual.valor)+'|<f2>}\"];\n'
            actual = actual.siguiente
            contador_nodos+=1

        #CREAR LOS ENLACES
        contador_nodos = 0
        actual = self.primero
        while contador_nodos < self.tamanio-1:
            codigodot += 'nodo'+str(contador_nodos)+':f2 -> nodo'+str(contador_nodos+1)+':f1[dir=both];\n'
            actual = actual.siguiente
            contador_nodos+=1
        
        #CREAMOS LOS ENLACES ENTRE EL PRIMERO Y EL ULTIMO
        codigodot += 'nodo0:f1 -> nodo'+str(self.tamanio-1)+':f2 [dir=both constraint=false];\n'

        codigodot += '}'

        #ESCRIBIMOS Y CREAMOS EL ARCHIVO DOT
        ruta_dot = 'reportesdot/listaDobleCircular.dot'
        archivo = open(ruta_dot,'w')
        archivo.write(codigodot)
        archivo.close()

        # GENERAMOS LA IMAGEN
        ruta_imagen = 'reportes/listaDobleCircular.jpg'
        comando = 'dot -Tjpg '+ ruta_dot + ' -o '+ ruta_imagen
        os.system(comando)

        #ABRIMOS LA IMAGEN
        ruta_abrir_imagen = os.path.abspath(ruta_imagen)
        os.startfile(ruta_abrir_imagen)