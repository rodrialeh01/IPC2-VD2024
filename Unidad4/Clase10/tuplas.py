# MANEJO DE TUPLAS

#1. CREAMOS UNA TUPLA
tupla_vacia = ()
print(tupla_vacia)

#2. CREAMOS UNA TUPLA CON 1 SOLO ELEMENTO
tupla_un_elemento = (1,) 
print(tupla_un_elemento)

#3. TUPLA CON VARIOS ELEMENTOS
tupla = (1,2,3,4,5)
print(tupla)

#4. TUPLA SIN PARENTESIS
tupla_sin_parentesis = 1,2,3,4,5,6,7,8
print(tupla_sin_parentesis)

#5. ACCEDER A LOS ELEMENTOS DE UNA TUPLA

#ACCEDIENDO POR INDIVIDUAL

primero = tupla[0]
print(primero)

ultimo = tupla[-1]
print(ultimo)

#6. ITERAR SOBRE UNA TUPLA

print('----------- ITERANDO SOBRE UNA TUPLA ---------')
for numero in tupla:
    print(numero)

#7. CORTAR UNA TUPLA

#7.1 OBTENER UNA SUBTUPLA
#:2 = < indice 2
subtupla = tupla[:2]
print(subtupla)

#1:4 = empieza desde el indice 1 hasta que el indice sea menor que 4
subtupla2 = tupla[1:4]
print(subtupla2)

#3: = desde el indice 3 hasta el final de la tupla
subtupla3 = tupla[3:]
print(subtupla3)

#8. CONCATENAR TUPLAS
tupla1 = ('hola','adios')
tupla2 = ('mundo', 'universo')
tupla3 = tupla1 + tupla2
print(tupla3)

#9. REPETIR EL MISMO VALOR DE UNA TUPLA
tupla4 = (20,40)
tupla5 = tupla4 * 6
print(tupla5)

#10. DESEMPAQUETAR UNA TUPLA

tupla6 = ('AB','CD')
var1,var2 = tupla6
print(var1)
print(var2)

#11. DESEMPAQUETO SOLO ALGUNOS ELEMENTOS
tupla7 = ('a','b','c','d','e','f')
v1, *v2 = tupla7
print(v1)
print(v2)

#12. COUNT
print('----- COUNT ----')
tupla8 = ('a','a','a','b','b','c','d')
conteo = tupla8.count('a')
print(conteo)

#13. INDEX
print('--- INDEX ---')
tupla9 = ('hola','mundo',':D','!')
indice = tupla9.index(':D')
print(indice)

#EDITAR UNA TUPLA
#no se pueden editar sus valores
print('--- EDITAR TUPLA ---')
tupla10 = (1,2,3,4,5,6,7)
tupla10[0] = 0
print(tupla10)