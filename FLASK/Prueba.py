from flask import Flask, render_template, url_for
import os



app = Flask(__name__)

empleados = ['Jorge', 'Juan', 'Pedro']


@app.route('/')

def holaMundo():
    
    return render_template('index.html', numeroEmpleados=len(empleados))

@app.route('/quienes')

def quienes():
    return 'Esta es la pagina de How About You'
'''
@app.route('/users/<string:nombreusuario>')

def users(nombreusuario):
    return 'Bienvenido ' + nombreusuario

'''

@app.route('/users/<int:numeroUser>')

def users(numeroUsuario):
    return 'Bienvenido usuario nº {} ' .format(numeroUsuario)


@app.route('/datosusuario/<int:id>/<string:nombre>')

def datosusuario(id, nombre):
    return 'Estos son los datos del usuario. Id: {}. Nombre: {}' .format(id, nombre)

@app.route('/posts')
@app.route('/posts/<int:numpost>')

def posts(numposts='null'):
    return 'Post nº: {}'.format(numposts)



if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug = True)