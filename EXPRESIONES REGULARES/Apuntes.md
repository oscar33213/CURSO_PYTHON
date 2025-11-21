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
