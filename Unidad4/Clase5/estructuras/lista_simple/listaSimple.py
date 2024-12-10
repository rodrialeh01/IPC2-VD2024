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