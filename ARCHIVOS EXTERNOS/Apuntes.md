# ARCHIVOS EXTERNOS

- La creación de archivos externos tiene como objetivo la **persistencia de datos**
- Posee dos alternativas:
  - Manejo de archivos externos
  - Trabajo con **BBDD**

- El manejo cuenta con **cuatro** fases:
    1. Creación
    2. Apertura
    3. Manipulación
    4. Cierre

- En este contexto la **apertura** y **cierre** se refiere a los **streams** que son los flujos de datos entre el documento y el codigo de **python**

## TRABAJO CON ARCHIVOS

- Creación de un archivo:

```python

from io import *
archivo_creado = open('primer_archivo.txt', 'w')

```

- Escritura en el archivo:

```python

from io import open
archivo_creado.write('Hola Mundo') #variable.write('Texto a escribor')
archivo_creado.close #CIERRA EL FLUJO DE DATOS

```

- Manipulación de archivos (**agregar contenido**):

```python

from io import *
#SE CREA EL ARCHIVO
rchivo_creado = open('primer_archivo.txt', 'w')
archivo_creado.write('Hola Mundo.')
archivo_creado.close
#SE MODIFICA EL ARCHIVO
archivo_creado = open('primer_archivo.txt', 'a')
archivo_creado.write('\nSegundo texto')
archivo_creado.close

```

- Leer el documento:

```python

from io import *
archivo_creado = open('primer_archivo.txt', 'w')
archivo_creado.write('Hola Mundo.')
archivo_creado.close
archivo_creado = open('primer_archivo.txt', 'r')

info_texto = archivo_creado.read() #VARIABLE DOND ESE ALMACENA EL CONTENIDO DEL TEXTO
archivo_creado.close()

print(info_texto)

```

- Leer grandes volumenes de texto

```python

from io import open 
archivo_creado2 = open('segundo_texto.txt', 'w')
archivo_creado2.write('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting')
archivo_creado2 = open('segundo_texto.txt', 'r')
texto = archivo_creado2.readline()
archivo_creado2.close()

print(texto)

```

## CURSOR

- Es la **posición** de donde se comenzara a leer el documento

```python

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

```

- Manejo del **cursor** en contexto

```python
from io import open

archivo_2 = open('Pruebas.txt', 'w')
archivo_2.write('Mi nombre es Oscar ')
archivo_2 = open('Pruebas.txt', 'r')
print(archivo_2.read())
archivo_2 = open('Pruebas.txt', 'a')

if archivo_2.seek(19):
    archivo_2 = open('Pruebas.txt', 'a')
    archivo_2.write('y tengo 28 años')
else:
    archivo_2 = open('Pruebas.txt', 'a')
    archivo_2.write('FEO')

archivo_2 = open('Pruebas.txt', 'r')

print(archivo_2.read())

```

```python

from io import open

primer_texto = input("Escribe el texto del documento: ")
segundo_texto = input("Escribe el texto que reemplazara al anterior: ")

archivo_creado = open('Archivo.txt', 'w')
archivo_creado.write(primer_texto)
archivo_creado = open('Archivo.txt', 'r')
print(archivo_creado.read())
archivo_creado.seek(0)  # <-- necesario para volver al inicio
longitud = len(archivo_creado.read())  # <-- guardar longitud
archivo_creado = open('Archivo.txt', 'r+')
archivo_creado.seek(int(longitud/2))
archivo_creado.write(segundo_texto)
archivo_creado = open('Archivo.txt', 'r')
print(archivo_creado.read())
archivo_creado.close()


```

## DIRECTORIOS

- Se trabaja con el modulo ***os***

### CREACION DE DIRECTORIOS

```python

import os

os.makedirs("PruebaDirectorio")

```

### MOVERSE ENTRE DIRECTORIOS

```python

import os

os.chdir("PruebaDirectorio")

```

### ELIMINAR UN ARCHIVO

```python
import os

os.chdir('Prueba')
os.remove('Pruebas2.txt')

```

### ELIMINAR UN DIRECTORIO

- En este codigo, analiza si el directorio esta vacio, si no lo esta, elimina el nombre del archivo indicado
- Una vez eliminado, si se vuelve a ejecutar elimina el directorio

```python

directorio = "Prueba"
archivo = os.path.join(directorio, "Prueba.txt")

if os.path.exists(directorio):
    if not os.listdir(directorio):  # está vacío
        os.rmdir(directorio)
        print(f"Directorio '{directorio}' eliminado porque estaba vacío.")
    else:  # no está vacío
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Archivo 'texto.txt' eliminado dentro de '{directorio}'.")
        else:
            print("El archivo 'texto.txt' no existe dentro del directorio.")
else:
    print(f"El directorio '{directorio}' no existe.")

```

- Este codigo elimina todos los archivos

```python

import os

directorio = "Prueba"
archivo = os.path.join(directorio, "Prueba.txt")

if os.path.exists(directorio):
    if not os.listdir(directorio):  # está vacío
        os.rmdir(directorio)
        print(f"Directorio '{directorio}' eliminado porque estaba vacío.")
    else:  # no está vacío
        if os.path.exists(archivo):
            os.remove(archivo)
            print(f"Archivo 'texto.txt' eliminado dentro de '{directorio}'.")
        else:
            print("El archivo 'texto.txt' no existe dentro del directorio.")
else:
    print(f"El directorio '{directorio}' no existe.")

```

### RENOMBRAR UN ARCHIVO

```python
import os
os.rename('Prueba.txt', 'Pruebas2.txt')

```

### CREAR UN ARCHIVO DENTRO DE UN DIRECTORIO

```python

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

    
```
