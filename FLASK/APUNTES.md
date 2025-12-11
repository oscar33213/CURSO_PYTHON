# FRAMEWORK: FLASK

---

## ¿Que es?

- Microframework escrito en **Python**
- Un **Framework** es la traducción de *Marco de Trabajo*

---

## ¿Par qué sirve?

- Se usa para crear aplicaciones web bajo **MVC** *(**M**ODELO **V**ISTA **C**ONTROLADOR)*
- El **MVC** consiste en crear una aplicacion siguiendo un **modulo concreto**:
  - **Modelo**: Sera la parte donde programaremos lo relacioando a los **datos** *(BBDD, Obtencion de datos...)*.
  - **Vista**: Programaremos todo lo relacionado a la interfaz *(Formularios...)*.
  - **Controlador**: Sera donde programaremos la logica que se encaragra de gestionar las peticiones *(Pone en comunicación los otros dos modulos)*.

---

## Django vs Flask

- Flask es mas sencillo
- Flask es mas veloz
- Django cuenta con funcionalidades *'por defecto'* que para pequeños proyectos son innecesarios

- Para una web simple, se usara **Flask**
- Para webs mas complejas con logica mas avanzada, se usara **Django**

---

## Caracteristicas de Flask

- Se adapta perfectamente a cada proyecto gracias a **extensiones**
- Incluye un **servidor propio** para **desarrollo** y **pruebas**
- **Rapido** y **Minimalista**
- **Facil** de usar y aprender
- Buena integración con varias herramientas utiles como:
  - **Jinja2:** Motor de plantillas web
  - **SQLAlchemy:** Herramienta SQL
- Compaltible con **WSGI**
- **OpenSource**
- Extensa documentación

---

## Documentación de Flask

[FlaskDocumentation](https://flask.palletsprojects.com/en/stable/)

---

## Instalación de Flask (Windows)

- Creamos un Entorno Virtual (No es obligado, pero si recomendado)

```bash

mkdir myproject
cd myproject
py -3 -m venv .venv

```

- Iniciamos el Entorno Virtual

```bash

.venv\Scripts\activate

```

- Instalamos Flask

``` bash

pip install Flask

```

- Codigo de ejemplo para saber si **Flask** esta correctamente instalado

```python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

```

---

## Instalación en MacOS/Linux

- Creación de Entorno Virtual

```bash
mkdir myproject
cd myproject
python3 -m venv .venv

```

- Activacion del Entorno Virtual

```bash
. .venv/bin/activate

```

- Instalación de Flask

```bash

pip install Flask

```

---

## Manejo de Flask

- Codigo ejemplo

```python
from flask import Flask 

app = Flask(__name__) 


@app.route('/')

def holaMundo():
    
    return 'Hola a todos'

```

- Para ejecutar cualquier programa de Flask lo haremos mediante la consola

```bash

flask --app NombreArchivo run

```

- Debera aparecer:

```bash

* Serving Flask app 'Nombre'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [03/Dec/2025 17:31:59] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Dec/2025 17:31:59] "GET /favicon.ico HTTP/1.1" 404 -

```

- Ahora una vez comprobado que **Flask** a sido instalado, procedemos a su uso

1. Dentro del directorio, crearemos una carpeta llamada *static*
2. Dentro de *'static'* crearemos otra carpeta llamada *css* *(Donde ira el .css)*
3. A su vez en la capeta raiz, crearemos una carpeta llamada *templates* *(Aqui ira el .html)*
4. Dentro de *'templates'* creamos un archivo HTML al que llamaremos *index.html*

--

## Vista de variables en el 'index.html'

- Podemos renderizar variables dentro de HTML
- Usaremos la nomenclatura clave:valor

```python

mpleados = ['Jorge', 'Juan', 'Pedro'] #Creamos la variable que se va a renderizar


@app.route('/')

def holaMundo():
    
    return render_template('index.html', numeroEmpleados=len(empleados)) #Como segundo argumento en el 'return' indicamos esa variable en formato calve:valor, es este caso queremos que se muestre la longitus de la lista

```

```html

  <br/>

    {{numeroEmpleados}}

```

---

## Activar el modo depurador

- Para arrancar el servidor en modo depurador hay que realizar una pequeña configuración dentro del programa

  - Importamos la libreria 'os'

  ```python

  import os

  ```

- Indicamos el siguiente codigo:

```python

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug = True)

```

- En este codigo indicamos que si lo almacenado en **name__* es la aplicación principal, esta la active en modo depuración
- Al hacer esto, iniciaremos la aplicación d ela siguiente manera:

```bash

python NombreApp.py

```

- Esto hara que no sea necesario para el servidor y reiniciarlo para visualizar los cambios

---

## Manejo de Parametros

```python

@app.route('/users/<string:nombreusuario>')

def users(nombreusuario):
    return 'Bienvenido ' + nombreusuario

```

- Estamos creando una pagina, dentro la la principal que al indicar la ruta '/users/Nombre' muestre un mensaje personalizado con el nombre
- Para ello en el decorador **'@app.route()'** indicamos la ruta y el tipo de dato que se maneja (en este caso, un string) seguido del nombre de la variable
- En la vista, recibira por parametro la variable creada en el decorador

---

## Dato por defecto

- En ciertas ocasiones, a la pagina web se le pasa un parametro innexistente, para ello se configura un dato **por defecto**
- **¡¡DISCLAIMER!!** Una vista, puede tener varios decoradores

```python

@app.route('/posts')
@app.route('/posts/<int:numpost>')

def posts(numposts='null'):
    return 'Post nº: {}'.format(numposts)

```

- En este caso, se indican **2 decoradores** uno de ellos sera el que actue cuando no se reciba un parametro, el segundo cuando lo haga
- En este caso, el la vista, se le aggregara un parametro por defecto, indicado *(variable='valor_por_defecto')* haciendo que arroje ese valor cuando reciba un parametro innexistente.

---

## Vinculos a vistas

- Podemos crear vinculos que redireccionen a diferentes vistas

```html

<br/>

    <a href="{{'quienes'}}">A la pagina de quienes</a>

```

- En este caso, en el HTML indicamos el nombre de la vista bajo **{{}}**

---

## URL_FOR (Apuntando a vistas y no a URL)

- Funcion de **FLASK** que perimte redireccionar teniendo en cuenta el nombre de la vista y no de la *url*
- Esto perimte que las *url* se puedan modificar sin verse alterada la vista

```html

<a href="{{url_for('posts')}}">Posts </a>

```

- Se indica el nombre de la vista, no de la *URL*

---

### URL_FOR Con parametros

```html

<a href="{{url_for('posts',numpost=1)}}">Post Nº1 </a>

```

- Los parametros se separaran con **,**

---

## Plantilla Base

- Son las que se usan para marcar el diseño que llevaran todas las paginas
- Para ello crearemos la plantilla con la siguiente estructura

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/index.css') }}">
    <title>{% block title %} {% endblock %}</title> 
</head>
<body>
    
    Contenido que queremos que sea igual en todas las paginas

    {%block content %}

    {% endblock %}
</body>
</html>

```

- En la etiqueta `<title>` estamos indicando que esta sera dinamica en función de la pagina donde nos encontremos
- En el **bloc-content** sera la zona donde ira cada bloque individual
- Una vez realizada la plantilla base, deberemos extenderla al resto

```html

{% extends "plantilla_base.html" %}

{% block title %} Sobre Nosotros {% endblock %}

{% block content %}

 (El html d ela pagina en si)

{% endblock %}

```

---

## Formularios

```html

<form action="" method="post">
<label>Nombre: </label>
<input type="text" id="nombre" name="nombre"/><br/>

<label>Telefono: </label>
<input type="number" id="numero" name="numero"/><br/>

<label>Email: </label>
<input type="email" id="email" name="email"/><br/>

<input type="submit" id="envio_form" name="envio_form" value="Enviar"/>

</form>

```

---
