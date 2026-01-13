from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, DateField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    Nombre = StringField(
        'Nombre',
        validators=[DataRequired(), Length(max=50)]
    )

    Telefono = StringField(
        'Telefono',
        validators=[DataRequired(), Length(max=12)]
    )

    Email = EmailField(
        'Email',
        validators=[DataRequired(), Length(max=50), Email()]
    )
    
    Mensaje = StringField(
        'Mensaje',
        validators=[DataRequired(), Length(max=500)]
    )

    submit = SubmitField('Enviar')


class PostForm(FlaskForm):
    Autor = StringField(
        'Autor',
        validators=[DataRequired(), Length(max=50)]
    )
    
    Post = StringField(
        'Post',
        validators=[DataRequired(), Length(max=500)]
    )
    
    
    BotonEnviar = SubmitField('Enviar')
    


class PostLogin(FlaskForm):
    
    User = StringField(
        'User',
        validators=[DataRequired(), Length(max=50)]
    )
    
    Password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=12)]
    )
    
    remember_me = BooleanField('Recuerdame')
    
    Logear = SubmitField('Login')
    
    
class RegisterIDPost(FlaskForm):
    
    User = StringField(
        'User',
        validators=[DataRequired()]
    )
    
    
    Email = EmailField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    
    Password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=12)]
    )
    
    remember_me = BooleanField('Recuerdame')
    
    BotonRegistro = SubmitField('Registrate')
    
    
    
