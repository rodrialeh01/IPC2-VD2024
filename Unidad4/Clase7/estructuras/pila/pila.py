import os

from estructuras.pila.nodo import Nodo


class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0
    
    #LONGITUD DE LA PILA
    def __len__(self):
        return self.tamanio

    #METODOS DE LA PILA
    #1. PUSH: INSERTAR UN ELEMENTO A LA PILA
    def push(self, valor):
        #1. CREAMOS EL NODO
        nuevo = Nodo(valor)
        #2. EL NUEVO NODO VA A TENER APUNTADO HACIA ABAJO LA CIMA
        nuevo.abajo = self.cima
        #3. LA NUEVA CIMA ES AHORA EL NUEVO NODO
        self.cima = nuevo
        #4. INCREMENTAMOS EL TAMAÑO DE LA PILA
        self.tamanio += 1
    
    #2. POP: ELIMINAR EL ELEMENTO DE LA PILA Y RETORNAMOS EL VALOR ELIMINADO
    def pop(self):
        #1. SI LA PILA ESTA VACIA NO SE ELIMINARÁ NADA Y RETORNARÁ NULO
        if self.cima == None:
            return None
        #2. GUARDAMOS EL VALOR DE LA CIMA
        nodo_que_se_elimina = self.cima.valor
        #3. LA NUEVA CIMA VA A SER EL NODO QUE ESTA ABAJO DE LA CIMA
        self.cima = self.cima.abajo
        #4. DISMINUIMOS EL TAMAÑO DE LA PILA
        self.tamanio -= 1
        #5. RETORNAMOS EL VALOR DEL NODO ELIMINADO
        return nodo_que_se_elimina

    #3. PEEK: MUESTRA EL VALOR DE LA CIMA
    def peek(self):
        if self.cima == None:
            return None
        return self.cima.valor
    
    #4. ISEMPTY: VERIFICA SI LA PILA ESTA VACIA
    def isEmpty(self):
        return self.cima == None
    
    #5. MOSTRAR Y RECORRER LA PILA
    def mostrar(self):
        if self.isEmpty():
            print("La pila está vacía")
            return
        
        actual = self.cima
        while actual != None:
            print(actual.valor)
            actual = actual.abajo
    
    #6. GRAFICAR
    def graficar(self):
        codigodot = ''
        codigodot += '''digraph G {
    rankdir=LR;
    node[shape=Mrecord];
    '''
        #CREAMOS EL NODO DE LA PILA
        codigodot += 'Pila[xlabel=\"Pila\" label=\"'
        #GRAFICAMOS LOS NODOS DE LA PILA
        actual = self.cima
        while actual != None:
            if actual.abajo != None:
                codigodot+=str(actual.valor) + '|'
            else:
                codigodot+=str(actual.valor)
            actual = actual.abajo
        codigodot+='\"];\n'
        codigodot+='}'

        #CREAMOS EL ARCHIVO DOT
        ruta_dot = 'reportesdot/pila.dot'
        archivo = open(ruta_dot,'w')
        archivo.write(codigodot)
        archivo.close()

        #GENERAMOS LA IMAGEN
        ruta_imagen = 'reportes/pila.png'
        comando = 'dot -Tpng '+ruta_dot+ ' -o '+ruta_imagen
        os.system(comando)

        #ABRIR LA IMAGEN
        ruta2 = os.path.abspath(ruta_imagen)
        os.startfile(ruta2)