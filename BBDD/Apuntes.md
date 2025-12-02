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

## CAMPO CLAVE

- Identificador unico a cada registro de entrada
- Para indicar que el campo va a ser **clave** se debera indicar en la creación la instrucción ***PRIMARY KEY***

```python

miCursor.execute('''
        CREATE TABLE PRODUCTOS_TIENDA(
        CODARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBREARTICULO VARCHAR(40),
        PRECIARTICULO INTEGER,
        SECCION VARCHAR(20)
        
        )
        
        ''')

```

- Si se intenta insertar un campo clave repetido, lanzara una excepcion de tipo ***UNIQUE***

```bash

UNIQUE constraint failed: TABLA.CAMPOCLAVE

```

### CAMPO CLAVE AUTOINCREMENTABLE

- Se espera que el campo clave, se autoincremente de manera gradual

```python

miCursor.execute('''
        CREATE TABLE PRODUCTOS_SUPERMERCADO(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ''')

productos = [
    ('Pasta', 2, 'Legumbres y Pastas'),
    ('Jabón', 3.45, 'Limpieza y Hogar')
]

miCursor.executemany('INSERT INTO PRODUCTOS_SUPERMERCADO VALUES (NULL,?,?,?)', productos)
miConexion.commit()

```

- Al indicar el *AUTOINCREMENT* le indicas que ese campo se incrementara en funcion las entradas

---

## ACTUALIZAR REGISTROS

- **Modificar** campos de registros **YA CREADOS**
- Si solo se va a actualizar un registro se recomienda hacerlo sobre el campo clave

```python

miCursor.execute('UPDATE NOMBRE_TABLA SET CAMPOAMODIFICAR=NUEVOVALOR WHERE ID=NUMEROCAMPOCLAVE')
miConexion.commit()

```

## BORRAR REGISTROS

```python

miCursor.execute('DELETE FROM PRODUCTOS_SUPERMERCADO WHERE ID=1')
miConexion.commit()

```

- La instrucción *DELETE* **SIEMPRE** debera ir junto a su clausula *WHERE* si no se eliminara **TODA** la tabla

---

### CLAUSULA UNIQUE

- Clausula que sirve para que ese campo no se pueda repetir en los registros

```python

miCursor.execute('''
        CREATE TABLE PRODUCTOS_TIENDA(
        CODARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBREARTICULO VARCHAR(40), UNIQUE
        PRECIARTICULO INTEGER,
        SECCION VARCHAR(20)
        
        )
        
        ''')

```

---

## MANEJO DE POSTGRESQL

### INSTALACIÓN DE POSTGRESQL

1. Se requerira descargar *postgresql*, para ello se debera buscar en el navegador
2. Accedemos a la pagina de *Descargas/Downloads*
3. Indicamos el **S.O**
4. Descaragmos el Instalador (*Se encuentra al principio de la pagina*)
5. Se recomienda descargar la **PENULTIMA** versión
6. Esperamos a que se descargue
7. Ejecutamos
8. En el proceso, indicas una contraseña y un puerto de escucha (Deberas recordarlos o apuntarlos para iniciar las futuras conexiones)
9. Una vez instalado, buscar *pgAdmin* y ejecutar

## CONEXION CON POSTGRESQL

- Se necesita una libreria de Python llamada *psycopg2*
- Para instalarla lo ahremos de la siguiente manera:

- Nos desplazamos a la carpeta donde estemos creando las **BBDD**

```bash

cd 'NombreCarpeta'

```

- Ejecuta:

```bash

pip install psycopg2

```

- Importa la libreria

```python

import psycopg2

```

- Si al importar falla, en el buscador buscaremos *'>python select interprete* y lo indicaremos
