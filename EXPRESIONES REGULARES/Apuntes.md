# EXPRESIONES REGULARES

## ¿Qué son?

- Conjunto o suma de funciones y secuencia de caracteres que nos permiten realizar búsquedas y crear patrones de búsqueda

## ¿Para que sirven?

- Búsqueda de texto utilizando patrones y funciones

## ¿Donde usarlas?

- **Búsqueda de texto** que se ahjusta a formatos
- Búsqueda de **existencia de texto**
- Nº de **coincidencias** dentro del texto
- ...

## ¿Como se usa?

- Estan almacenadas en el modulo *re*

```python

import re
cadena = 'Estoy trabajando con Python en Domingo y Semana Santa'
print(re.search('domingo', cadena.lower()))

```

- Uso en condicionales:

```python

import re

cadena = 'Estoy trabajando con Python en Domingo y Semana Santa'

busqueda = 'Domingo'

if re.search(busqueda.lower(), cadena.lower()) is not None:
    print(f'Se encontro el {busqueda}')
else:
    print('No se encontro')

```

### Funciones *Start* & *End*

- Sirven no solo para buscar en el texto, si no tambien para localizarlo

```python

import re

cadena = 'Estoy trabajando con Python en Domingo y Semana Santa'
busqueda = 'domingo'

texto_encontrado = re.search(busqueda, cadena, re.IGNORECASE)

print(texto_encontrado.start())
print(texto_encontrado.end())

```

### Funcion *findall*

- Expresion que busca **TODAS** las coincidencias de una palabra

```python

cadena = 'Estoy trabajando con Python en Domingo y Semana Santa. El proximo Domingo no pienso estudiar'
busqueda = 'domingo'
print(re.findall(busqueda, cadena, re.IGNORECASE))

```

- Podemos contar las veces que aparece una palabra con *findall*

```python

import re

cadena = 'Estoy trabajando con Python en Domingo y Semana Santa. El proximo Domingo no pienso estudiar'
busqueda = 'domingo'
veces_apear = (len(re.findall(busqueda, cadena, re.IGNORECASE)))
print(f'La palabra {busqueda.capitalize()} aparece: {veces_apear} veces')


```

## Metacaracteres

- Los metacaracteres en Python sirven para definir patrones flexibles y potentes que permiten buscar, validar y manipular texto usando expresiones regulares
- Uso de **^**:

```python

import re

lista_nombres = [
    'Mateo Ruz',
    'Juan Hidalgo',
    'Pedro Pascal',
    'Luis Diaz',
    'Pedro Perez',
    'Jorge Nitales',
    'Mateo Russo',
    'Nacho Hidalgo']

for nombre in lista_nombres:
    if re.findall('^Pedro', nombre):
        print(nombre)
    else:
        print('No hay coincidencias')
```

- Uso de **$**:

```python
import re

lista_nombres = [
    'Mateo Ruz',
    'Juan Hidalgo',
    'Pedro Pascal',
    'Luis Diaz',
    'Pedro Perez',
    'Jorge Nitales',
    'Mateo Russo',
    'Nacho Hidalgo']
for nombres in lista_nombres:
    if re.findall('o$', nombres):
        print(nombres)
    else:
        print('No hay coincidencias')

```

- Uso de **[]**

```python
import re

lista_terminos = [
    'Camión',
    'Camion',
    'Niños',
    'Niñas',
    'Ejemplo'
]

for lista in lista_terminos:
    if re.findall('cami[oó]n', lista.lower()):
        print(lista)
    else:
        print('No hay coincidencias')

```

- Uso combinado de **^** y **$**

```python

import re

dominios = [
    "example.com",
    "google.com",
    "openai.com",
    "example.es",
    "github.com",
    "wikipedia.org",
    "elpais.es",
    "stackoverflow.com",
    "openai.es",
    "elpais.es"   
    ]

for dominio in dominios:
    if re.search('^e', dominio):
        print(dominio)
    else:
        print('No hay coincidencias')
        
print('--------')

for dominio in dominios:
    if re.search('.com$', dominio):
        print(dominio)
    else: 
        print('No hay coincidencias')

```

- Hay varias expresiones regulares:

  - **.**: Coincide con **cualquier carácter** excepto salto de línea.
  - **^**: Marca el **inicio** de la cadena.
  - **$**: Marca el **final** de la cadena.
  - **'*'**: Repite el patrón **0** o **más veces**.
  - **+**: Repite el patrón **1** o **más veces**.
  - **?**: Hace el patrón **opcional (0 o 1 vez)** o lo vuelve **no-greedy** según contexto.
  - **{n}**: Coincide con el patrón **exactamente n veces**.
  - **{n,}**: Coincide **al menos n veces**.
  - **{n,m}**: Coincide **entre n y m veces**.
  - **[]**: Define un **conjunto de caracteres permitidos**
  - **[^ ]**: Conjunto **negado** (cualquier carácter excepto los incluidos).
  - **|**: Operador **OR** entre patrones.
  - **()**: **Agrupa patrones** y **captura su contenido**.
  - **'\'**: **Escapa metacaracteres** o introduce secuencias especiales **(\d, \w, etc.)**.
  - *etc...*

### Rangos

- Busca coincidencias que abarquen los rangos seleccionados

```python

import re
#RANGOS
lista_terminos = [
    'Camión',
    'Camion',
    'Niños',
    'Niñas',
    'Ejemplo'
]
#Buscara las coincidencias entre las letras 'p' y 'z'
for lista in lista_terminos:
    if re.findall('[p-z]', lista.lower()):
        print(lista)
    else:
        print('No hay coincidencias')

```

- Podemos hacer que busque rangos que empiecen por *n* caracter:

```python
import re

lista_terminos = [
    'Camión',
    'Camion',
    'Niños',
    'Niñas',
    'Ejemplo'
]
for lista in lista_terminos:
    if re.findall('^[a-j]', lista.lower()):
        print(lista)
    else:
        print('No hay coincidencias')


```

```python

import re

lista_productos = [
        'Ma1',
        'Se1',
        'Ma2',
        'Va1',
        'Ca1',
        'Ma3',
        'Ma4',
        'Se2']

for producto in lista_productos:
    if re.findall('Ma[1-3]', producto, re.IGNORECASE):
        print(producto)
    else:
        print('No hay coincidencias')

```

- En este ejemplo busca un numero determinado de rango (del 1 al 3), ignorando cuantos mas hay
- Tambien podemos buscar rangos entre letras y numeros:

```python

import re

lista_productos = [
        'Ma1',
        'Se1',
        'Ma2',
        'Va1',
        'Ca1',
        'Ma3',
        'Ma4',
        'Se2',
        'SeA',
        'SeB',
        'Va2',
        'SeC']

for producto in lista_productos:
    if re.findall('Se[0-2A-B]', producto, re.IGNORECASE):
        print(producto)
    else:
        print('No hay coincidencias')

```

### Funcion *match* $ *search*

- **Match**: Realiza la busqueda al comienzo del termino donde se quere realizar la busqueda
- **Search**: Realiza la busqueda en todo el *string*

- Uso de *match*

```python

import re

nombre1 = 'Lionel Messi'
nombre2 = 'Kylian Mbappé'
nombre3 = 'Zlatan Ibrahiovic'


if re.match('Kylian', nombre1, re.IGNORECASE):
    print(f'Esta en el 1º')
elif re.match('Kylian', nombre2, re.IGNORECASE):
    print('Esta en el 2º')
elif re.match('Kylian', nombre3, re.IGNORECASE):
    print('Esrta en el 3º')
else:
    print('No esta')

```

- Uso de *search*:

```python

import re

nombre1 = 'Lionel Messi'
nombre2 = 'Kylian Mbappé'
nombre3 = 'Zlatan Ibrahiovic'

if re.search('L', nombre1, re.IGNORECASE):
    print(True, f'{nombre1}')
else:
    print(False)

```
