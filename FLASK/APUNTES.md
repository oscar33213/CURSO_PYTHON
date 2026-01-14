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

- Si queremos hacer que los formularios, recojan la información y la almacenen, deberemos autorizarlo en el **decorador** indicando el ``method``

```python

@app.route('/contacto', methods=['GET', 'POST'])

```

- Si estas trabajndo en **Linux** deberas importar una libreria para poder usar ``methods``

```python

from crypt import methods

```

- En **Windows** dara error

---

### Mostrar los datos capturados en el formulario

- Se necesita el uso de ``request``
- Para ello habra que importarlo

```python

from flask import request

```

- Existen diversas formas de capturar, pero usaremos la mas simple, con sentencia ``if``

```python

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        campo1 = request.form['NombreCampo1']
        campo2 = request.form['NombreCampo2'] #EN EL request.form[] TENDREMOS QUE PONER EL NOMBRE QUE SE LE DIO EN LA PLANTILLA DEL FORMULARIO
        campo3 = request.form['NombreCampo3']

        return redirect(url_for('PagPrin'))
        
        
    return render_template('contacto.html')

```

---

### Validación de formularios

- Se usa para verificar que los campos han sido **rellenados** de manera correcta
- Para ello se usaran **dos librerias**
  - *Flask-WTF* [Documentación_Flask] (<https://flask-wtf.readthedocs.io/en/1.2.x/>)
  - *email validator*
- Se requiere previamnete que se instalen

```bash
pip install Flask-WTF

```

```bash

pip install email-validator

```

- **Flask-WTF** tiene protección para ataques de [CSRF] (<https://www.fortinet.com/lat/resources/cyberglossary/csrf>)

- Para usuarlo, seguirmos los siguientes pasos:

1. A la altura donde ese encuentre nuestra app principal, crearemos un archivo **.py** llamado *forms.py*
2. Dentro de el archivo crearemos el sigueinte codigo:

```python

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('nombreUser', validators=[DataRequired(), Length(max=50)])
    phoneNumber = IntegerField('numeroUser', validators=[DataRequired(), Length(max=12)])
    email = EmailField('emailUser', validators=[DataRequired(), Length(max=50), Email()])
    
    submit = SubmitField('envio_form')

```

- Una vez hecho eso, en la vista donde este el formulario,mdeberemos hacer varias modificaciones

- Vista antes del **Validator**

```python
@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        campo1 = request.form['NombreCampo1']
        campo2 = request.form['NombreCampo2'] #EN EL request.form[] TENDREMOS QUE PONER EL NOMBRE QUE SE LE DIO EN LA PLANTILLA DEL FORMULARIO
        campo3 = request.form['NombreCampo3']

        return redirect(url_for('PagPrin'))
        
        
    return render_template('contacto.html')

```

- Vista **DESPUES** del **Validator**

```python

from forms import SignupForm

app.config['SECRET_KEY']='TUCONTRASEÑA'

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = SignupForm()
    if form.validate_on_submit():
        nombreUser = form.name.data
        numeroUser = form.phoneNumber.data
        emailUser = form.email.data
        
        numero_oculto = "*****" + numeroUser[-4:]
        email_oculto = '*' * (len(emailUser)- 4) + emailUser[-4]
        
        
        
        return redirect(url_for('PagPrin'))
        
        
    return render_template('contacto.html', form=form)
```

- Ahora cogera la información de los campos del archivo *forms.py*

- Deberemos modificar la plantilla:

```html
<form action="" method="post" novalidate>
    {{ form.hidden_tag() }}

    {{ form.name.label }}
    {{ form.name(size=20) }}
    {% for error in form.name.errors %}
        <span style="color: red;">{{ error }}</span>
        
    {% endfor %}
    <br/>

    {{ form.phoneNumber.label }}
    {{ form.phoneNumber(size=15) }}
    {% for error in form.phoneNumber.errors %}
        <span style="color: red;">{{ error }}</span>
        
    {% endfor %}
    <br/>
    {{ form.email.label }}
    {{ form.email(size=20) }}
    {% for error in form.email.errors %}
        <span style="color: red;">{{ error }}</span>
        
    {% endfor %}
    <br/>
    {{ form.submit() }}
</form>

```

## Capturar el Usuario

- Se puede crear un sistema de **Login** y **Registro** para limitar accesos a ciertas zonas
- Para ello nos apoyaremos en una libreria llamada **Flask-Login** la cual deberemos instalar

### Instalar flask-login

```bash
cd carpetaProyectoFlask
pip install flask-login
```

- Se recomienda paarar elservidor y reiniciar VSCode

## LoginManager

- Es la clase que permitira operar con los inicios de sesion
- Se creara una instancia que sera accesible desde cualquier punto de la pagina

```python

from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY']=''

login_manager = LoginManager(app)

```

- Deberemos crear una clase Usuario
- Para que funcione necestaremos tener registardas una serie de propiedades
- Para ello, dentro d ela carpeta raiz del pryecto, crearemos un archivo llaamdo *models.py*
- Dentro de *models.py* crearemos la clase Usuario

```python
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id, name, email, passwd, is_admin=False):
        
        self.id = id
        self.name = name
        self.email = email
        self.passwd = passwd
        self.is_admin = is_admin
        
    def setPassword(self, passwd):
        self.passwd = generate_password_hash(passwd)
        
    def check_password(self, passwd):
        return check_password_hash(self.passwd,passwd)
```

- Una vez en el archivo de las vistas, crearemos lo sigueinte:

```python

@login_manager.user_loader

def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None

```

- Modificaremos la vista del Login

```python
from flask_login import LoginManager, current_user
from models import users, get_user
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('PagPrin'))
    
    form = PostLogin()
    
    if form.validate_on_submit():
        user = get_user(form.User.data)
        
        if user is not None and user.check_password(form.Password.data):
            load_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('PagPrin')
            return redirect(next_page)

    return render_template('login.html', form=form)
```

- En *models.py* crearemos lo siguiente

```python
users =  []


def get_user(email):
    for user in users:
        if user.email == email:
            return user
    return None
```

- **¡¡¡Esto es solo para capturar los registrsos de sesión en una lista, la version final se vera cuando implementemos una BBDD!!!**

'''

## IMPLEMENTACIÓN DE BBDD EN FLASK

- Para poder trabajar con un SGBBD (En este caso *PostgreSQL*) deberemos realizar una serie de pasos:
- Instalar un paquete en VS CODE

```bash
pip install flask-sqlalchemy
```

- Esto permitira la conexion a la BBDD
- Una vez realizado esta instalación, deberemos descargar PostgreSQL (Si no lo tenemos)
- Una vez instalado, buscamos PGAdmin en Windows
- Deveremos instalar otro paquete

```bash
pip install psycopg2

```

- Ahora en app.py deberemos importar la libreria

```python

from flask_sqlalchemy import SQLAlchemy

```

- Ahora deberemos introducir la ruta de PostGreeSQL en *app.py*

```python

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:contraseña@localhost:puerto/nombrebbdd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #PERMITE QUE CUANDO HAGAMOS MODIFICACIONES EN LAS BBDD, EMITA UNA SEÑAL
database = SQLAlchemy(app)

```

'''

## CONEXION CON LA BBDD - FLASK

### USO DE ORM (OBJECT RELATIONAL MODEL)

- Es la acción de usar los registros de las BBDD usando la regla de los Objetos con los **pradigamas de la POO**

- En *models.py* deberemos crear el constructor

```python
from flask_login import UserMixin, LoginManager
login_manager = LoginManager()
class User(UserMixin, db.Model):
    
    __tablename__ = 'Usuarios_pagina'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    is_admin = db.Column(db.Boolean, default = False)
        
    def setPassword(self, password):
        self.passwd = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

```

- En el archivo *app.py* deberemos añadir una serie de variables

```python

    login_manager.init_app(app)

    db.init_app(app)
```

- Necesitamos que cuando la app se inicie, esta cree las tablas, esto lo haremos de la siguiente manera
- En *app.py*

```python
@app.before_first_request
def create_table():
    db.create_all()
```

## Modificación de una vista

```python
@app.route('/registrate', methods=['GET', 'POST'])
def registrate():
    
    if current_user.is_authenticated:
        return redirect(url_for('PagPrin'))
    
    form = RegisterIDPost()
    
    if form.validate_on_submit():
        
        usuario = form.User.data
        email = form.Email.data
        password = form.Password.data
        remember = form.remember_me.data
        
        user = User(email = email, user = usuario)
        user.setPassword(password)
        
        
        #login_user(user, remember=remember)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('registrate.html', form=form)

```

- Aquie crearemos la ventana de Registro
- Para crear la ventana de login y que esta rescate de la *BBDD* lo haremos de la siguiente manera

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('PagPrin'))
    
    form = PostLogin()
    
    if form.validate_on_submit():
        usuario = request.form['user'] # Rescatamos de la columna 'Usuario'
        userTrue = User.query.filter_by(user=usuario).first() #Buscamos si existe ese usuario en la BBDD
        
        if userTrue is not None and userTrue.check_password(request.form['password']): #Si existe, logueamos
            login_user(userTrue)
            
    
    

    return render_template('login.html', form=form)

```
