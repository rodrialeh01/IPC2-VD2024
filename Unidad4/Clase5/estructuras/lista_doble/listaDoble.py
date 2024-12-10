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
        return None
    
    def login(self, id,pwd):
        actual = self.primero
        while actual != None:
            if actual.valor.id == id and actual.valor.password == pwd:
                return True
        return False