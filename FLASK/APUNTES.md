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
