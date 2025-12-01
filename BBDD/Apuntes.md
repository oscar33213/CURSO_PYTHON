# BASES DE DATOS

---

## TIPOS DE SGBD SOPORTADAS

- *SQLServer*
- *Oracle*
- *MySQL*
- *SQLite*
- *PostgresSQL*
- *...*

- Para manejar **bases de datos** es necesario conocer el **lenguaje SQL**

---

## SQLite

- **Ventajas:**
  - SGBD Relacional
  - Escrito en *C*
  - Forma **parte integral** del programa
  - Codigo abierto
  - Se guarda como un **unico fichero** en el host
  - Ocupa **poco espacio**
  - Eficiente y rapido
  - **Multiplataforma**
  - Dominio publico

- **Desventajas:**
  - No admite clausulas anidadas (*WHERE*)
  - No existen usuarios
  - Sin clave foranea en *modo consola*

---

## CONEXION A UNA BBDD

1. **Abrir** o **Crear** la conexión.
2. Crear el **puntero**
3. Ejecutar el **query** (*Consulta*)
4. **Manejar** los resultados de la consulta (*Sistema CRUD* **C**REATE, **R**EAD, **U**PDATE, **D**ELETE)
5. **Cerrar** el puntero
6. **Cerrar** la conexión

---

## MANEJO DE SQLite3

```python

import sqlite3

#CREAR LA CONEXIÓN
miConexion = sqlite3.connect('D:\CURSO PYTHON TUTORIZADO\BBDD/miBase') 

#CREAR EL CURSOR
miCursor = miConexion.cursor()
#EJECUTAR EL QUERY
miCursor.execute('CREATE TABLE PRODUCTOS (NARTICULO VARCHAR (50),PRECIO INTEGER, SECCION VARCHAR (20))') #OJO UNA VEZ SE EJECUTE, SE COMENTA O SE BORRA
#INSERTAR REGISTROS
miCursor.execute('INSERT INTO PRODUCTOS VALUES("Camiseta", 25, "MODA")')
#VERIFICAR REGISTRO
miConexion.commit()
#CERRAR EL CURSOR
miCursor.close()
#CERRAR LA CONEXIÓN
miConexion.close()

```

---

## INSERTAR VARIOS PRODUCTOS

- Se pueden crear *Querys* de varios productos a la vez

```python

#INSERTAR VARIOS REGISTROS
muchosProductos = [
    ('Patin', 100, 'Deportes'),
    ('Cenicero', 20, 'Ceramica'),
    ('Pantalón', 80, 'Moda')
]

miCursor.executemany('INSERT INTO PRODUCTOS VALUES(?,?,?)', muchosProductos)
miConexion.commit()
#CERRAR EL CURSOR
miCursor.close()
#CERRAR LA CONEXIÓN
miConexion.close()
```

---

## CONSULTA DE BBDD

- Se usa la instrucción *SELECT*
- No requiere del *commit* dado que no se esta modificando la tabla

```python

#CONSULTA
miCursor.execute('SELECT* FROM PRODUCTOS')
listaProductos = miCursor.fetchall() #CONVIERTE LOS CAMPOS A UNA LISTA

print(listaProductos)



```

- Otra forma de recorrer la lista

```python

miCursor.execute('SELECT* FROM PRODUCTOS')
listaProductos = miCursor.fetchall()

for p in listaProductos:
    print(f'Nombre: {p[0]}\nPrecio: {p[1]}€\nSección: {p[2]}.')

```

---
