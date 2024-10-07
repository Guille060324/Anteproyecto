from flask import Flask, render_template, redirect, url_for, flash # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from forms import RegistroForm, LoginForm, CredencialForm
from models import Usuario, Credencial, Coleccion
from passlib.hash import sha256_crypt # type: ignore
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        hashed_password = sha256_crypt.hash(form.contraseña.data)
        usuario = Usuario(usuario=form.usuario.data, contraseña=hashed_password,
                          nombre=form.nombre.data, apellido=form.apellido.data,
                          celular=form.celular.data, correo=form.correo.data)
        db.session.add(usuario)
        db.session.commit()
        flash('Usuario registrado con éxito')
        return redirect(url_for('login'))
    return render_template('registro.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(usuario=form.usuario.data).first()
        if usuario and sha256_crypt.verify(form.contraseña.data, usuario.contraseña):
            flash('Inicio de sesión exitoso')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dashboard():
    return 'Bienvenido al Dashboard'

@app.route('/nueva_credencial', methods=['GET', 'POST'])
def nueva_credencial():
    form = CredencialForm()
    if form.validate_on_submit():
        credencial = Credencial(sitio=form.sitio.data, correo=form.correo.data,
                                usuario=form.usuario.data, contraseña=form.contraseña.data,
                                coleccion_id=form.coleccion_id.data, nota=form.nota.data)
        db.session.add(credencial)
        db.session.commit()
        flash('Credencial guardada con éxito')
        return redirect(url_for('dashboard'))
    return render_template('nueva_credencial.html', form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
