from flask import Flask, render_template, request, redirect,url_for
import mysql.connector #el code no me funciona con el from controller.controllerSucursal import * con este nomas
#importando las funciones
from controller.controllerSucursal import *
from controller.controllerEmpleados import *

app = Flask(__name__)

#conexion a BD lo mismo que el archivo conexionBD.py
db = mysql.connector.connect(
    # host="sql.freedb.tech",
    # user="freedb_db_test_111",
    # passwd="4JKtwGf@DQD@b?w",
    # database="freedb_db_pharmacy"
    host ="127.0.0.1",
    user ="root",
    passwd ="gordillo303132x",
    database = "db_pharmacy"
)

@app.route('/')
def index():
    return render_template('index.html')


#Sucursal
################################################################
@app.route('/sucursal',methods=['GET','POST'])
def sucursalView():
    # Obtenemos la lista de sucursales
    return render_template('sucursales.html', lista = listaSucursales())

@app.route('/add_Sucursal', methods=['POST'])
def add_Sucursal():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    realizado = registrarSucursal(nombre,direccion,telefono)
    return redirect(url_for('sucursalView'))

@app.route('/delete_sucursal/<string:id>')
def delete_sucursal(id):
    eliminarSucursal(id)
    return redirect(url_for('sucursalView'))

@app.route('/edit_sucursal/<string:id>')
def edit_sucursal(id):
    return render_template('edit-sucursal.html', data = getSucursal(id))

@app.route('/update_sucursal/<string:id>', methods=['POST'])
def update_sucursal(id):
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    updateSucursal(nombre,direccion,telefono,id)
    return redirect(url_for('sucursalView'))

#Empleado
################################################################
@app.route('/empleados')
def empleados():
    # Obtenemos la lista de empleados
    empleados = listaEmpleados()

    # Pasamos la lista de empleados como argumento a la plantilla empleados.html
    return render_template('empleados.html', miData=empleados)

@app.route('/add_Empleado', methods=['POST'])
def add_Empleado():
    # Recibimos los datos enviados mediante el formulario
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']
    dia = request.form['dia']
    mes = request.form['mes']
    anio = request.form['anio']
    contrato_fecha = f"{anio}-{mes}-{dia}"
    id_sucursal = request.form['ID_sucursal']

    # Llamamos a la función "registrarEmpleado" y pasamos los datos recibidos
    realizado = registrarEmpleado(nombre, apellido, direccion, telefono, email, contrato_fecha, id_sucursal)

    # Redirigimos a la vista "empleados"
    return redirect(url_for('empleados'))

@app.route('/empleados_vista')
def empleados_vista():
    empleados = listaEmpleados()
    return render_template('empleados_vista.html', miData=empleados)

@app.route('/buscar_empleado', methods=['POST'])
def buscar_empleado():
    correo = request.form['correo']
    empleado = obtenerEmpleadoPorCorreo(correo)
    return render_template('empleados_vista.html', miData=[empleado])

@app.route('/editar_empleado/<int:id_empleado>', methods=['GET', 'POST'])
def editar_empleado(id_empleado):
    if request.method == 'POST':
        # Obtén los datos enviados mediante el formulario de edición
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        id_sucursal = request.form['ID_sucursal']

        # Llama a una función que actualice los datos del empleado en la base de datos
        # Pasando los nuevos valores y el ID del empleado a editar
        actualizarEmpleado(id_empleado, nombre, apellido, direccion, telefono, email, id_sucursal)

        # Redirige a la página de empleados después de la edición
        return redirect(url_for('empleados_vista'))
    else:
        # Obtiene el empleado por su ID para mostrar los datos actuales en el formulario de edición
        empleado = obtenerEmpleadoPorID(id_empleado)
        return render_template('editar_empleado.html', empleado=empleado)

@app.route('/borrar_empleado/<int:id_empleado>', methods=['POST'])
def borrar_empleado(id_empleado):
    # Llama a una función que borre al empleado de la base de datos
    eliminarEmpleado(id_empleado)

    # Redirige a la página de empleados después de borrar al empleado
    return redirect(url_for('empleados_vista'))

#Producto
################################################################
# Ruta principal que muestra todos los productos
@app.route('/productos')
def mostrar_productos():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Producto")
    productos = cursor.fetchall()
    return render_template('productos.html', productos=productos)

# Ruta para agregar un producto
@app.route('/agregar_producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        stock_cantidad = int(request.form['stock_cantidad'])
        id_marca = int(request.form['id_marca'])
        id_categoria = int(request.form['id_categoria'])
        id_sucursal = int(request.form['id_sucursal'])
        id_receta = int(request.form['id_receta'])

        cursor = db.cursor()
        cursor.execute("INSERT INTO Producto (nombre, descripcion, precio, stock_cantidad, ID_marca, ID_categoria, ID_sucursal, ID_receta) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (nombre, descripcion, precio, stock_cantidad, id_marca, id_categoria, id_sucursal, id_receta))
        db.commit()
        return redirect('/productos')
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Marca")
        marcas = cursor.fetchall()
        cursor.execute("SELECT * FROM Categoria")
        categorias = cursor.fetchall()
        cursor.execute("SELECT * FROM Sucursal")
        sucursales = cursor.fetchall()
        cursor.execute("SELECT * FROM Receta")
        recetas = cursor.fetchall()
        return render_template('agregar_producto.html', marcas=marcas, categorias=categorias, sucursales=sucursales, recetas=recetas)

# Ruta para eliminar un producto
@app.route('/eliminar_producto/<int:id>', methods=['POST'])
def eliminar_producto(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Producto WHERE ID_producto = %s", (id,))
    db.commit()
    return redirect('/productos')


if __name__ == '__main__':
    app.run(debug=True)
