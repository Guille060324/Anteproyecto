from flask_sqlalchemy import SQLAlchemy # type: ignore
from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    celular = db.Column(db.String(15), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)

class Coleccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

class Credencial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sitio = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    coleccion_id = db.Column(db.Integer, db.ForeignKey('coleccion.id'), nullable=False)
    nota = db.Column(db.Text, nullable=True)
