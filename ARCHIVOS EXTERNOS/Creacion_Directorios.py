import os
from io import open

os.makedirs("PruebaDirectorio", exist_ok=True)  # evita error si ya existe
os.chdir("PruebaDirectorio")

nombreDirectorio = os.getcwd()
try:
    if os.path.exists(nombreDirectorio):
        texto = input("Escribe el texto: ")
        texto_2 = input("Escribe el segundo texto: ")

        # Escritura
        with open('Texto.txt', 'w', encoding='utf-8') as archivo:
            archivo.write(texto + '\n')

        # Lectura inicial
        with open('Texto.txt', 'r', encoding='utf-8') as archivo:
            textoin = archivo.read()
            
        # Añadir segundo texto
        with open('Texto.txt', 'a', encoding='utf-8') as archivo:
            archivo.write(texto_2)

        # Lectura final
        with open('Texto.txt', 'r', encoding='utf-8') as archivo:
            textoin = archivo.read()        

        print(textoin)
    else:
        print(f'Directorio {nombreDirectorio} no encontrado')
except FileNotFoundError:
    print('Archivo no encontrado')


