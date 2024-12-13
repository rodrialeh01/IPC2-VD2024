from pila import Pila

pila = Pila()

pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)

pila.graficar()

print('Eliminando a' , pila.pop())