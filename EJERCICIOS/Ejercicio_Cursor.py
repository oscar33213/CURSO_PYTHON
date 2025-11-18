from io import open

primer_texto = input("Escribe el texto del documento: ")
segundo_texto = input("Escribe el texto que reemplazara al anterior: ")
tercer_texto = input("Escribe el tercer texto: ")

archivo_creado = open('Archivo.txt', 'w')
archivo_creado.write(primer_texto + "\n")
archivo_creado.write(segundo_texto + "\n")   # ← ahora también agregamos el segundo texto
archivo_creado = open('Archivo.txt', 'r+')
lista_archivo = archivo_creado.readlines()

# Asegurar que existe una tercera línea (índice 2)
while len(lista_archivo) < 3:
    lista_archivo.append("\n")

lista_archivo[2] = tercer_texto + "\n"   # ← sustituye la tercera línea

archivo_creado.seek(0)
archivo_creado.writelines(lista_archivo)
archivo_creado.close()











