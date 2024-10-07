from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField # type: ignore
from wtforms.validators import DataRequired, Email, Length # type: ignore

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    celular = StringField('Celular', validators=[DataRequired()])
    usuario = StringField('Usuario', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')

class CredencialForm(FlaskForm):
    sitio = StringField('Sitio', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    usuario = StringField('Usuario', validators=[DataRequired()])
    contraseña = PasswordField('Contraseña', validators=[DataRequired()])
    coleccion_id = IntegerField('ID de Colección', validators=[DataRequired()])
    nota = TextAreaField('Nota')
    submit = SubmitField('Guardar')
