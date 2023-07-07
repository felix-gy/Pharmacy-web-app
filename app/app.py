from flask import Flask, render_template, request, redirect,url_for
#importando las funciones
from controller.controllerSucursal import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sucursal')
def sucursal():
    # Obtenemos la lista de sucursales
    # La enviamos como argumento de la forma: dato = dato
    return render_template('sucursales.html', miData = listaSucursales())

@app.route('/add_Sucursal', methods=['POST'])
def add_Sucursal():
    #recivimos los datos
    direccion = request.form['direccion']
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    realizado = registrarSucursal(direccion,nombre,telefono)
    # retornamos a nuestra vista sucursales
    return redirect(url_for('sucursal'))

# @app.route('/empleado')
# def empleado():
#     return render_template('empleado.html',the_title='Farmacia')

if __name__ == '__main__':
    app.run(debug=True)