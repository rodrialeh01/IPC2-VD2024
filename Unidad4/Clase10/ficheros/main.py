# MANEJO DE FICHEROS

#1. MÉTODO DE LECTURA DE FICHEROS
print('--------- LECTURA DE ARCHIVOS --------------')
with open('lectura.txt','r', encoding='utf-8') as archivo:
    contenido_a_leer = archivo.read()
    print('El contenido del archivo es: ', contenido_a_leer)

#2. MÉTODO PARA ESCRITURA DE FICHEROS
print('--------- ESCRITURA DE ARCHIVOS --------------')
with open('escritura.txt','w') as archivo:
    contenido_a_escribir = 'Acabo de lograr escribir en un nuevo archivo :DDDDD'
    archivo.write(contenido_a_escribir)

#3. MÉTODO PARA AÑADIR TECTO A UN FICHERO
print('--------- AÑADIR TEXTO A UN ARCHIVO --------------')
with open('añadir.txt','a') as archivo:
    contenido_a_agregar = 'Rodrigo'
    archivo.write(contenido_a_agregar)

#4. MÉTODO PARA UN ARCHIVO EN MODO LECTURA Y ESCRITURA
print('--------- LECTURA Y ESCRITURA DE ARCHIVOS --------------')
with open('lectura_escritura.txt','r+', encoding='utf-8') as archivo:
    contenido_a_leer = archivo.read()
    print('Leyo del archivo: ', contenido_a_leer)
    contenido_a_agregar = '\n1. Tomate\n2. Manzanas\n3. Cocos'
    nuevo_contenido = contenido_a_leer + contenido_a_agregar
    archivo.write(nuevo_contenido)
    print('Se actualizo el archivo')

#5. QUIERO POSICIONARME EN UN PUNTO ESPECIFICO DEL ARCHIVO
#SEEK 
#ESCRIBIR
print('--------- POSICIONARME EN UN PUNTO ESPECIFICO DEL ARCHIVO ---------')
with open('lectura_escritura.txt', 'r+', encoding='utf-8') as archivo:
    #primero escribimos el texto
    archivo.seek(38)
    archivo.write('\n0. Prueba\n')
    print('Se actualizo el archivo')

#LEER
with open('lectura_escritura.txt','a+', encoding='utf-8') as archivo:
    archivo.seek(6)
    lee = archivo.read()
    print('leyo: ', lee)

#LEER LINEA POR LINEA
with open('nuevo.txt', 'r', encoding='utf-8') as archivo:
    contador = 0
    for linea in archivo:
        print(f'Linea {contador}: {linea}')
        contador += 1
    
