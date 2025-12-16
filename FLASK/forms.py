from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField(
        'nombreUser',
        validators=[DataRequired(), Length(max=50)]
    )

    phoneNumber = StringField(
        'numeroUser',
        validators=[DataRequired(), Length(max=12)]
    )

    email = EmailField(
        'emailUser',
        validators=[DataRequired(), Length(max=50), Email()]
    )

    submit = SubmitField('envio_form')
