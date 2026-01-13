from flask import Flask, render_template, url_for, request, redirect
import os
from datetime import datetime
from forms import ContactForm, PostForm, PostLogin, RegisterIDPost
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from models import User, users, get_user


app = Flask(__name__)

app.config['SECRET_KEY']='OscarHidalgo#332199713'

login_manager = LoginManager(app)

login_manager.login_view = 'login'

posts_guardados = []


@app.route('/')

def PagPrin():
    
    return render_template('index.html')

@app.route('/quienes')

def quienes():
    return render_template('conocenos.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    if form.validate_on_submit():
        Nombre = form.Nombre.data
        Telefono = form.Telefono.data
        Email = form.Email.data
        Mensaje = form.Mensaje.data
        
        
        
        return redirect(url_for('PagPrin'))
        
        
    return render_template('contacto.html', form=form)

@app.route('/servicios')
@login_required

def servicios():
    return render_template('servicios.html')

@app.route('/productos')
@login_required
def productos():
    return render_template('Productos.html')


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    form = PostForm()
    if form.validate_on_submit():
        
        posts_guardados.append({
            "autor": current_user.name,
            "contenido": form.Post.data,
            "fecha": datetime.now()
        })
        # Redirige a la misma página para limpiar el formulario
        return redirect(url_for('posts'))

    # Renderizamos la página con el formulario y los posts actuales
    return render_template('posts.html', form=form, posts=posts_guardados)


@app.route('/PagPosts')

def PagPosts():
    return render_template('PagPosts.html', posts=posts_guardados)


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('PagPrin'))
    
    form = PostLogin()
    
    if form.validate_on_submit():
        user = get_user(form.User.data)
        
        if user is not None and (user.check_password(form.Password.data) == form.Password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page:
                next_page = url_for('PagPrin')
            return redirect(next_page)

    return render_template('login.html', form=form)

@app.route('/registrate', methods=['GET', 'POST'])
def registrate():
    
    form = RegisterIDPost()
    
    if form.validate_on_submit():
        
        usuario = form.User.data
        email = form.Email.data
        password = form.Password.data
        remember = form.remember_me.data
        
        # Cambiar 'user' por 'users' para contar cuantos hay
        user = User(len(users) + 1, usuario, email, password)
        users.append(user)
        login_user(user, remember=remember)  # load_user → login_user
        return redirect(url_for('PagPrin'))
    
    return render_template('registrate.html', form=form)




@login_manager.user_loader

def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/logout')

def logout():
    logout_user()
    return redirect(url_for('PagPrin'))

if __name__ == "__main__":
    os.environ['FLASK_ENV'] = 'development'
    app.run(debug = True)