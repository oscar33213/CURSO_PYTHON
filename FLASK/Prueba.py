from flask import Flask, render_template, url_for, request, redirect
import os
from datetime import datetime
from forms import ContactForm, PostForm, PostLogin, RegisterIDPost
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from models import User, db, login_manager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'OscarHidalgo#332199713'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5433/proyectoflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager.init_app(app)
db.init_app(app)

login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



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
        return redirect(url_for('posts'))

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
        usuario = form.User.data
        password = form.Password.data

        userTrue = User.query.filter_by(user=usuario).first()

        if userTrue and userTrue.check_password(password):
            login_user(userTrue, remember=form.remember_me.data)
            return redirect(url_for('PagPrin'))

    return render_template('login.html', form=form)



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

        user = User(email=email, user=usuario)
        user.setPassword(password)

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('registrate.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('PagPrin'))


if __name__ == "__main__":
    app.config["ENV"] = "development"

    with app.app_context():
        db.create_all()

    app.run(debug=True)
