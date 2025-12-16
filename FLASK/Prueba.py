from flask import Flask, render_template, url_for, request, redirect
import os

from forms import SignupForm



app = Flask(__name__)

app.config['SECRET_KEY']='OscarHidalgo#332199713'

@app.route('/')

def PagPrin():
    
    return render_template('index.html')

@app.route('/quienes')

def quienes():
    return render_template('conocenos.html')

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

@app.route('/servicios')

def servicios():
    return render_template('servicios.html')

@app.route('/productos')

def productos():
    return render_template('Productos.html')





if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug = True)