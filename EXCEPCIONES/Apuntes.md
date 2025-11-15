# 🐍 Python: Excepciones y manejo de errores

## 1. ¿Qué son las excepciones?

Las excepciones son errores que ocurren durante la ejecución de un programa.  
Python permite capturarlas y tratarlas para evitar que el programa se detenga abruptamente.

---

## 2. Captura básica de excepciones

Usamos `try` y `except` para manejar errores comunes.

```python
try:
    numero = int("abc")  # ValueError
except ValueError:
    print("❌ No se pudo convertir a entero")
```

---

## 3. Tratamiento completo con else y finally

Podemos añadir bloques `else` y `finally` para controlar el flujo.

```python
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("❌ División entre cero")
else:
    print("✅ Resultado:", resultado)
finally:
    print("🔚 Siempre se ejecuta este bloque")
```

---

## 4. Múltiples excepciones

Podemos capturar distintos tipos de errores.

```python
try:
    lista = [1, 2, 3]
    print(lista[5])  # IndexError
except IndexError:
    print("❌ Índice fuera de rango")
except TypeError:
    print("❌ Tipo de dato incorrecto")
```

---

## 5. Crear excepciones personalizadas

Podemos definir nuestras propias reglas de error.

```python
class EdadNegativaError(Exception):
    pass

def verificar_edad(edad):
    if edad < 0:
        raise EdadNegativaError("La edad no puede ser negativa")

try:
    verificar_edad(-3)
except EdadNegativaError as e:
    print("❌ Error personalizado:", e)
```

---

## 6. Diagrama de flujo (ASCII)

``` ascii

        ┌───────────────┐
        │     try       │
        └───────┬───────┘
                │
        ¿Error ocurre?
          /       \
        Sí         No
        │          │
   ┌────▼────┐   ┌─▼─────┐
   │ except  │   │ else  │
   └────┬────┘   └─┬─────┘
        │          │
        └──────┬───┘
               │
          ┌────▼────┐
          │ finally │
          └─────────┘
```

---

## 7. Resumen rápido

- `try`: bloque que puede generar errores  
- `except`: captura errores específicos  
- `else`: se ejecuta si no hay errores  
- `finally`: se ejecuta siempre  
- `raise`: lanza una excepción manualmente  
- `class MiError(Exception)`: define una excepción personalizada  

---
