import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:contraseña@localhost/nombre_base_datos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
