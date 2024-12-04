# Este es un comentario simple

'''
este
es
un
comentario
multi
linea
salu2
ipc2
'''

"""
este
es
otro
comentario
multi
linea
salu2
"""

# Declaración de variables

hola = "Hola"
x = 10
y = 32
z = 45
a = True
b = False
c = 9.99
d = []
e = {}
f = None


# Asignación de variables

ipc2 = "IPC2"
ipc2 = "Introducción a la Programación y Computación 2"

variable = 1
variable = "1"
variable = True
variable = 4.5
variable = [1,2,3,4]

# Casteo

var1 = "1"
var2 = int(var1)
var3 = 4
var4 = str(var3)
var5 = "2.45"
var6 = float(var5)

# Expresiones aritméticas

# Suma
suma = 3+3
#ERROR
# concat = 3 + "hola"
#CORRECTO
concat = str(3) + "hola"

# Resta
resta = 2-6

# Multiplicacion
multiplicacion = 2*3

# Division
division = 3/2

# Modulo
modulo = 4%2

# Expresiones de incremento y decremento

#x++
x += 1 # x = x + 1
#x--
x -= 1 # x = x - 1
#x**
x *= 2 # x = x * 2
#x/
x /= 2 # x = x / 2
#x%
x %= 2 # x = x % 2

# Operaciones relacionales

x < y
x > y
x <= y
x >= y
x == y
x != y # x ! = y

# Operaciones Lógicas

a and b # &&
c or d # ||
not e # !

# Outputs
# Sin salto de linea
print("Hola mundo! :D", end="")
# Con salto de linea
print("Hola de nuevo")

# Inputs

# Caso tipado
#entrada = int(input("Ingresa algo: "))

# Caso no tipado
#entrada = input("Ingresa tu nombre: ")
#print("Hola, mi nombre es " + entrada)

#input("entrada porque si")

# Condicional IF

condicional = 5

if condicional > 5:
    print("Es mayor que 5")
elif condicional == 5:
    print("Es igual a 5")
else:
    print("Es menor que 5")

# Match-case

dia = 2

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("No coincide con ninguno")

# Ciclo While
contador = 1
print("Ciclo While")
while contador <= 10:
    print(contador)
    contador+=1

# Ciclo FOR
print("Ciclo For")
#contador de numeros
# Range i = 1; i < 10
for i in range(1,11):
    print(i)

#contador 2
# range j = 0; j < 10
for j in range(10):
    print(j)

# iterar una lista
lista = [1,2,3]

for numero in lista:
    print(numero)

for z in range(len(lista)):
    print(lista[z])

# Funciones

#Sin parametros y sin retornar
def funcion1():
    print("Hola ipc2!")

funcion1()

#Con parametros y sin retornar
def funcion2(num1, num2):
    total = num1+num2
    print("La suma de num1 y num2 es: " + str(total))

funcion2(1,2)

#sin parametros y retorna algo
def funcion3():
    return 2+891584784*8/2-5542187

print(funcion3())

#con parametros y con retorno
def funcion4(num1,num2):
    return num1-num2

print(funcion4(6,1))

# funcion tipada
def funcion5(num1:int, num2:int) -> int:
    return num1 * num2

print(funcion5(6, 7))