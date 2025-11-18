from io import *
archivo_creado = open('primer_archivo.txt', 'w')
archivo_creado.write('Hola Mundo.')
archivo_creado = open('primer_archivo.txt', 'a')
archivo_creado.write('\nSegundo texto')
archivo_creado.write('\nTercer Texto')
archivo_creado = open('primer_archivo.txt', 'r')
print(archivo_creado.read())
archivo_creado.seek(0) #POSICION DEL CURSOR AL PRINCIPIO
print(archivo_creado.read())
archivo_creado.seek(11) #POSICION DEL CURSOR AL CARACTER 11
print(archivo_creado.read())


# SEEK VS READ

#archivo_creado.seek(len(archivo_creado.read())/2)
#print(archivo_creado.read())

archivo_creado.seek(int(len(archivo_creado.readline())/2))

print(archivo_creado.read())


