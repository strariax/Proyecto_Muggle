from flask_sqlalchemy import SQLAlchemy

# Inicializar la extension SQLALCHEMY

db = SQLAlchemy()

# Definimos una clase que representa una tabla en la base de datos

class Registro(db.Model): # Heredando de la clase 
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellido = db.Column(db.String(20), nullable=False)
    fecha_de_nacimiento = db.Column(db.String, nullable = False)
    ciudad = db.Column(db.String, nullable = False)
    barrio = db.Column(db.String, nullable = False)
    numero_contacto = db.Column(db.Integer, nullable = False)

    # Constructor de clase

    def __init__(self, nombre, apellido, fecha_de_nacimiento, ciudad, barrio, numero_contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.ciudad = ciudad
        self.barrio = barrio
        self.numero_contacto = numero_contacto
