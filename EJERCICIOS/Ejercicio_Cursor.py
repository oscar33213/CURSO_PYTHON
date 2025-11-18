from io import open

primer_texto = input("Escribe el texto del documento: ")
segundo_texto = input("Escribe el texto que reemplazara al anterior: ")


archivo_creado = open('Archivo.txt', 'w')
archivo_creado.write(primer_texto)
archivo_creado = open('Archivo.txt', 'r')
print(archivo_creado.read())
archivo_creado.seek(0)
archivo_creado = open('Archivo.txt', 'w')
archivo_creado.write(segundo_texto)
archivo_creado = open('Archivo.txt', 'r')
print(archivo_creado.read())
archivo_creado.close()




