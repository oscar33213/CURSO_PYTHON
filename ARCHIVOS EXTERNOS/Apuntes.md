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
archivo_creado.seek(0)
archivo_creado = open('Archivo.txt', 'w')
archivo_creado.write(segundo_texto)
archivo_creado = open('Archivo.txt', 'r')
print(archivo_creado.read())
archivo_creado.close()


```
