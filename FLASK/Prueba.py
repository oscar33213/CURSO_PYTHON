from flask import Flask, render_template, url_for
import os



app = Flask(__name__)



@app.route('/')

def PagPrin():
    
    return render_template('index.html')

@app.route('/quienes')

def quienes():
    return render_template('conocenos.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/servicios')

def servicios():
    return render_template('servicios.html')

@app.route('/productos')

def productos():
    return render_template('Productos.html')





if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug = True)