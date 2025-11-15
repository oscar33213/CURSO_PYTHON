# 🐍 Python: Sintaxis básica y estructuras fundamentales

## 1. Variables

Una variable es un nombre que almacena un valor. No necesitas declarar el tipo.

```python
x = 10          # Entero
nombre = "Ana"  # Cadena
pi = 3.14       # Decimal
activo = True   # Booleano
```

## 2. Sintaxis básica

Python usa **indentación** para estructurar el código.

```python
def saludar():
    print("Hola, mundo")
```

### Comentarios

```python
# Comentario de una línea

"""
Comentario
de varias líneas
"""
```

## 3. Condicionales

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")
```

## 4. Bucles

### Bucle for

```python
for i in range(5):
    print("Número:", i)
```

```python
frutas = ["manzana", "banana", "uva"]
for fruta in frutas:
    print(fruta)
```

### Bucle while

```python
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```

## 5. Listas

```python
numeros = [10, 20, 30]
print(numeros[0])       # Acceder a un elemento

numeros.append(40)      # Añadir
numeros.remove(20)      # Eliminar
```

## 6. Tuplas

```python
coordenadas = (10, 20)
print(coordenadas[0])
# coordenadas[0] = 30  # ❌ Error: no se puede modificar
```

## 7. Diccionarios

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

print(persona["nombre"])        # Acceso
persona["edad"] = 26            # Modificar
persona["email"] = "ana@mail.com"  # Añadir clave
```

## 8. Funciones

```python
# Función simple
def saludar():
    print("Hola!")

saludar()

# Función con parámetros
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print("Resultado:", resultado)

# Función con valor por defecto
def presentar(nombre, edad=18):
    print(f"Me llamo {nombre} y tengo {edad} años.")

presentar("Laura")
presentar("Carlos", 25)

# Función con varios valores de retorno
def coordenadas():
    return 10, 20

x, y = coordenadas()
print(x, y)
```
