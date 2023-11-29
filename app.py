from flask import render_template, request, redirect, url_for
from conexion import app, db
from models import Registro

@app.route('/')
def index():
    return render_template('index.html')

# CRUD (Crear, Leer, Actualizar, Eliminar)

@app.route('/formulario_adoptar', methods = ['POST', 'GET'])

def formulario_adoptar():

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha_de_nacimiento = request.form['fecha_de_nacimiento']
        ciudad = request.form['ciudad']
        barrio = request.form['barrio']
        numero_contacto = request.form['numero_contacto']

        # Creamos un objeto de la clase empleados con los datos obtenidos

        datos_padrinos = Registro(nombre, apellido, fecha_de_nacimiento, ciudad, barrio, numero_contacto)

        db.session.add(datos_padrinos)
        db.session.commit()

        return render_template('formulario_adoptar.html')

    return render_template('formulario_adoptar.html')

@app.route('/ranking')

def ranking():

    print("Funciona")

    return render_template('ranking.html')

@app.route('/elegir_arbol')

def elegir_arbol():

    return render_template('elegir_arbol.html')

@app.route('/nosotros')

def nosotros():

    return render_template('nosotros.html')

@app.route("/pago")

def pago():

    if request.method == 'POST':

        return render_template('pago.html')
    
    return render_template('pago.html')

@app.route('/gracias')

def gracias():

    return render_template('gracias.html')

@app.route('/adoptar')

def adoptar():

    return render_template('adoptar.html')

@app.route('/login')

def login():

    return render_template('login.html')

@app.route('/perfil_arbol')

def perfil_arbol():

    return render_template('perfil_arbol.html')





'''
@app.route('/mostrar_datos', methods = ['GET', 'POST'])
def mostrar_datos():
    lista_empleados = Empleados.query.all()
    return render_template('mostrar_datos.html', lista_empleados=lista_empleados)

@app.route('/actualizar/<int:empleado_id>', methods=['GET','POST'])
def actualizar(empleado_id):
    empleado_a_actualizar = Empleados.query.get(empleado_id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cedula = request.form['cedula']
        edad = request.form['edad']

        empleado_a_actualizar.nombre = nombre
        empleado_a_actualizar.apellido = apellido
        empleado_a_actualizar.cedula = cedula
        empleado_a_actualizar.edad = edad

        db.session.commit()

        return redirect(url_for('mostrar_datos'))
    
    return render_template("actualizar.html", empleado_a_actualizar=empleado_a_actualizar)

@app.route('/eliminar', methods = ['GET','POST'])
def eliminar():
    if request.method == 'POST':
        id = request.form['empleado_id']
        empleado_a_eliminar = Empleados.query.filter_by(id=id).first()

        db.session.delete(empleado_a_eliminar)
        db.session.commit()

        return redirect(url_for('mostrar_datos'))

'''
    
if __name__ == ("__main__"):
    app.run(debug = True, port=8000)