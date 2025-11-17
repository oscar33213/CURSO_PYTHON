# **ESTRUCTURA DE DATOS**

## Tipos de Estructura de Datos

### ***Conjuntos***

- Un conjunto **(o *set*)** es una **colección no ordenada** de elementos **sin repetición**.
- Como consecuencia:

  - No admiten indexación.
  - No registran la posición de los elementos.
  - No mantienen un orden de inserción.

- Usos:
  - Comprobar la existencia de un elemento conjunto
  - Eliminar entradas **duplicadas**
  - Crear un codigo mas **eficiente** y **legible**

- Ejemplo de codigo usando ***set***

```python

SSolar = 'Mercurio, Venus, Tierra, Marte, Jupiter, Saturno, Urano, Neptuno, Pluton' #LISTA DE ELEMENTOS (STRING)
# SET
planetas = set()
#BUCLE QUE RECORRE EL STRING Y CREA LA LISTA
for planeta in SSolar.split(', '): #SEPARADOR (SE INDICA EL USADO EN EL STRING)  
    planetas.add(planeta)
print(planetas)
```

- Este codigo devuelve lo mismo sin usar el bucle for:
- Pero cambaira el resultado, creando un conjunto con cada caracter del **string** eliminando los caracteres repetidos

```python

SSolar = 'Mercurio, Venus, Tierra, Marte, Jupiter, Saturno, Urano, Neptuno, Pluton' #LISTA DE ELEMENTOS (STRING)
# SET
planetas = set(SSolar)
print(planetas)
```

### ***Colas o Queues***

- Existen **tres** tipos de colas
  - FIFO (***F***IRST ***I***N ***F***IRST ***O***UT)

```python
  import queue
miCola = queue.Queue()
miCola.put("Madrid")
miCola.put("Barcelona")
miCola.put("Valencia")
```

- LIFO (***L***AST ***I***N ***F***IRST ***O***UT)

```python
miCola_2 = queue.LifoQueue()
miCola_2.put("Madrid")
miCola_2.put("Barcelona")
miCola_2.put("Valencia")

print("Siguientes elementos: ")

for elemento in miCola_2.queue:
    print(elemento)

```

- **Priority** (Los elementos tiene una prioridad que se debera indicar)

```python

miCola_3 = queue.PriorityQueue()
miCola_3.put((3,"Madrid"))
miCola_3.put((2,"Barcelona"))
miCola_3.put((1, "Valencia"))


for elemento in miCola_3.queue:
    print(elemento)

```

- La clase **queue** cuenta con diferentes metodos:
  - *qsize()*
  - *empty()*
  - *full()*
  - *put()*
  - *put_nowait()*
  - *get()*
  - *get_nowait()*
  - *task_done()*
  - *join()*

```python
print(cola.full())
```

```python
#USO DE METODO EN CONTEXTO
cola = queue.Queue(4) 
numero = 1
while not cola.full():
    cola.put(f'El numero es: {numero}')
    numero += 1

for elem in cola.queue:
    print(elem)

```

- Se le puede agregar un limite de elementos a las colas

```python

cola = queue.Queue(4) #EL PARAMETRO INDICA QUE LA COLA SOLO TENDRA '4' ELEMENTOS
cola.put("1")
cola.put("2")
cola.put("3")
cola.put("4")
for elem in cola.queue:
    print(elem)

```
