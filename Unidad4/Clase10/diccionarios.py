# MANEJO DE DICCIONARIOS

#1. CREAMOS UN DICCIONARIO
#DICCIONARIO VACIO

nuevo = {}

#DICCIONARIO CON DATOS INICIALES
diccionario = {
    'nombre':'Rodrigo',
    'edad': 23,
    'pais':'Guatemala'
}

#POR MEDIO DEL CONSTRUCTOR
nuevo_dic = dict()

#2. ACCEDER A LOS DATOS DEL DICCIONARIO
print(diccionario['nombre'])

#3. MODIFICAR LOS VALORES
diccionario['nombre'] = 'Rodri'
print(diccionario)

#4. AÑADIMOS UN NUEVO PAR CLAVE-VALOR
diccionario['universidad'] = 'USAC'
diccionario['curso'] = 'IPC2'
diccionario['videojuegos'] = [
    {
        'nombre': 'Valorant'
    },
    {
        'nombre': 'Minecraft'
    }
]

print(diccionario)

#5. ELIMINAMOS UN PAR CLAVE-VALOR
print('------------ ELIMINAMOS UN CLAVE-VALOR --------------')
del diccionario['curso']
print(diccionario)

#6. ITERAMOS EN UN DICCIONARIO
print('------------ ITERAMOS EN UN DICCIONARIO --------------')
for clave, valor in diccionario.items():
    print('CLAVE: ', clave)
    print('VALOR: ', valor)

#7. ITERAMOS SOBRE LAS CLAVES
print('------------ ITERAMOS SOBRE LAS CLAVES --------------')
for clave in diccionario:
    print(clave)

#8. ITERAMOS SOBRE LOS VALORES
print('------------ ITERAMOS SOBRE LOS VALORES --------------')
for valor in diccionario.values():
    print(valor)

#9. COMPROBAMOS SI EXISTE UNA CLAVE
if 'curso' in diccionario:
    print('La clave existe')
else:
    print('La clave no existe')

#10. GET
print('------------ GET --------------')
edad = diccionario.get('edad')
print('La edad es ', edad)
#CON EXCEPCIONES
curso = diccionario.get('curso','Ninguna')
print('El curso es ', curso)

#11. KEYS
print('------------ KEYS --------------')
claves = diccionario.keys()
print('Las claves son ', claves)

#12. VALUES
print('------------ VALUES --------------')
valores = diccionario.values()
print('Los valores son ', valores)

#13. ITEMS
print('------------ ITEMS --------------')
items = diccionario.items()
print('Los items son ', items)

#14. LIMPIAR O ELIMINAR LOS VALORES DEL DICCIONARIO
print('------------ LIMPIAR O ELIMINAR LOS VALORES DEL DICCIONARIO --------')
diccionario.clear()
print(diccionario)