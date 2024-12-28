class NodoCelda:
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor
        self.arriba = None
        self.abajo = None
        self.izquierda = None
        self.derecha = None