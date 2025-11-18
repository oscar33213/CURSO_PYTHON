from io import *
#CREACION DE ARCHIVO
#nombre_variable = open(#nombre_archivo, w = write; r = read; a = action)
archivo_creado = open('primer_archivo.txt', 'w')

#ESCRITURA DE ARCHIVO

archivo_creado.write('Hola Mundo.') #variable.write('Texto a escribor')
archivo_creado.close #CIERRA EL FLUJO DE DATOS

#AGREGAR INFORMACIÓN


archivo_creado = open('primer_archivo.txt', 'a')
archivo_creado.write('\nSegundo texto')
archivo_creado.close

#LECTURA

archivo_creado = open('primer_archivo.txt', 'r')

info_texto = archivo_creado.read()
archivo_creado.close()

print(info_texto)

#LECTURA GRANDES VOLUMENES DE DATOS

archivo_creado2 = open('segundo_texto.txt', 'w')
archivo_creado2.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. \nLorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer \ntook a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting')
archivo_creado2 = open('segundo_texto.txt', 'r')
texto = archivo_creado2.readlines()
archivo_creado2.close()

print(texto[2])



