from flask import Flask, render_template, request, redirect,url_for
from datetime import date
import random
import mysql.connector #el code no me funciona con el from controller.controllerSucursal import * con este nomas
#importando las funciones
from controller.controllerSucursal import *
from controller.controllerEmpleados import *
from controller.controllerCliente import *
from controller.controllerProducto import *
from controller.controllerCategoria import *
from controller.controllerTransaccion import *

from controller.controllerFarmacia import *

db = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = ""
)

app = Flask(__name__)
#Farmacia
################################################################
@app.route('/')
def index():
    data = listaFarmacia()
    print(data)
    return render_template('index.html', data = data)

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

@app.route('/empleados_vender/<int:id_empleado>', methods=['GET', 'POST'])
def empleados_vender(id_empleado):
    if request.method == 'POST':
        nombre_producto = request.form['nombre_producto']
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Producto WHERE nombre LIKE %s", ('%' + nombre_producto + '%',))
        productos = cursor.fetchall()
        return render_template('empleados_vender.html', productos=productos)
    else:
        # Obtener los datos del empleado según el ID_empleado utilizando obtenerEmpleadoPorID
        empleado = obtenerEmpleadoPorID(id_empleado)

        cursor = db.cursor()
        cursor.execute("SELECT * FROM Producto")
        productos = cursor.fetchall()

        return render_template('empleados_vender.html', empleado=empleado, productos=productos)
 
@app.route('/empleados_venta/<int:id_empleado>')
def empleado_venta(id_empleado):
    ventas = obtenerVentasRealizadasPorEmpleado(id_empleado)
    return render_template('empleados_venta.html', ventas=ventas)


#transaccion
################################################################
@app.route('/vender', methods=['GET', 'POST'])
def vender():
    if request.method == 'POST':
        # Obtener los datos del formulario de búsqueda
        producto_id = request.args.get('producto_id')

        # Buscar el producto por ID
        producto = obtener_producto_por_id(producto_id)

        # Verificar si se encontró el producto
        if producto:
            # Renderizar la plantilla con el producto encontrado
            return render_template('cliente_compra.html', empleados=empleados, producto_id=producto['ID_producto'])
        else:
            # Renderizar la plantilla con un mensaje de error
            return render_template('vender.html', error=True)
    else:
        # Obtener todos los productos
        productos = obtener_productos()

        # Renderizar la plantilla con todos los productos
        return render_template('vender.html', productos=productos)



@app.route('/guardar_transaccion', methods=['POST'])
def guardar_transaccion():
    if request.method == 'POST':
        tipo = request.form['tipo']
        cantidad = request.form['cantidad']
        id_venta = request.form['ID_venta']
        id_compra = request.form['ID_compra']
        id_factura = request.form['ID_factura']

        # Obtener los datos de la venta y la compra
        venta = obtener_venta_por_id(id_venta)
        compra = obtener_compra_por_id(id_compra)

        # Generar IDs aleatorios para empleado y factura
        id_empleado = random.randint(1000, 10000)
        id_factura = random.randint(1000, 10000)

        # Realizar la inserción en la tabla de ventas de empleados
        insertar_venta_empleado(venta['fecha'], venta['total'], id_empleado, venta['ID_producto'])

        # Realizar la inserción en la tabla de compras de clientes
        insertar_compra_cliente(compra['fecha'], compra['total'], compra['ID_cliente'], compra['ID_producto'])

        # Generar la factura utilizando los IDs de venta y compra
        generar_factura(id_venta, id_compra, id_factura)

        # Obtener los datos de la factura generada
        factura = obtener_factura_por_id(id_factura)

        # Realizar la inserción en la tabla de facturas
        insertar_factura(factura['fecha'], factura['total'], factura['ID_cliente'])

        # Redireccionar a la página de éxito o mostrar mensaje de confirmación
        # ...

        return "Transacción guardada exitosamente"  # O puedes redirigir a otra página

    # Manejar el caso si no se realiza una solicitud POST
    return "Acceso denegado"  # O puedes redirigir a una página de error


@app.route('/cliente_compra')
def cliente_compra():
    empleados = listaEmpleados()  # Obtener la lista de empleados
    producto_id = request.args.get('producto_id')  # Obtener la ID del producto desde la URL
    precio = "{:.2f}".format(float(request.args.get('precio')))

    return render_template('cliente_compra.html', empleados=empleados, producto_id=producto_id, precio=precio)


@app.route('/add_cliente_compra', methods=['POST'])
def agregar_cliente_compra():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        id_sucursal = request.form['ID_sucursal']
        id_empleado = request.form['ID_empleado']
        id_producto = request.form['ID_producto']
        precio = request.form['precio']

        # Obtener el último ID de cliente utilizado
        ultimo_id_cliente = obtener_ultimo_id_cliente()

        # Generar el siguiente ID de cliente sucesivo
        nuevo_id_cliente = ultimo_id_cliente + 1

        # Insertar los datos en la tabla Cliente
        crear_cliente(nombre, apellido, direccion, telefono, email, id_sucursal)

        # Generar IDs únicos para las transacciones
        id_venta = random.randint(10000, 100000)
        id_compra = random.randint(10000, 100000)
        id_factura = random.randint(10000, 100000)

        # Generar el tipo de transacción (por ejemplo, "Compra" o "Venta")
        tipo_transaccion = "Compra"  # Puedes ajustar esto según tus necesidades

        # Generar la fecha actual
        fecha_actual = date.today().strftime("%Y-%m-%d")

        # Calcular el total de la venta y la compra en base al precio del producto
        total_venta = float(precio)
        total_compra = float(precio)

        # Resto de la lógica para agregar las transacciones a la base de datos
        # ...

        # Insertar los datos en la tabla Venta_empleado
        insertar_venta_empleado(id_venta, fecha_actual, total_venta, id_empleado, id_producto)

        # Insertar los datos en la tabla Compra_cliente
        insertar_compra_cliente(id_compra, fecha_actual, total_compra, nuevo_id_cliente, id_producto)

        # Insertar los datos en la tabla Factura
        insertar_factura(id_factura, fecha_actual, total_venta, nuevo_id_cliente)

        # Obtener los datos de la factura recién generada
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Factura ORDER BY ID_factura DESC LIMIT 1")
        factura_data = cursor.fetchone()
        # Insertar los datos en la tabla Transaccion_compra_venta
        cursor.execute("INSERT INTO Transaccion_compra_venta (tipo, cantidad, ID_venta, ID_compra, ID_factura) VALUES (%s, %s, %s, %s, %s)",
                    (tipo_transaccion, 1, id_venta, id_compra, id_factura))
        db.commit()

        # Crear el diccionario de la factura
        factura = {
            'ID_factura': id_factura,
            'fecha': fecha_actual,
            'total': total_venta,
            'ID_cliente': nuevo_id_cliente,
            'tipo_transaccion': tipo_transaccion
        }


        # Redireccionar a la página de detalles de la factura
        return render_template('factura.html', factura=factura)


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
        fecha_vencimiento = request.form['fecha_vencimiento']
        id_marca = int(request.form['id_marca'])
        id_categoria = int(request.form['id_categoria'])
        id_receta = int(request.form['id_receta'])
        id_distribuidor = int(request.form['id_'])

        cursor = db.cursor()
        cursor.execute("INSERT INTO Producto (nombre, descripcion, precio, fecha_vencimiento, ID_marca, ID_categoria, ID_receta, ID_distribuidor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (nombre, descripcion, precio, fecha_vencimiento, id_marca, id_categoria, id_receta, id_distribuidor))
        db.commit()

        # Obtener el ID del producto recién creado
        producto_id = cursor.lastrowid

        # Crear una entrada en el inventario para el nuevo producto
        cursor.execute("INSERT INTO Inventario (producto_id, cantidad) VALUES (%s, %s)",
                       (producto_id, 0))  # Inicialmente, la cantidad en inventario se establece en 0
        db.commit()

        return redirect('/productos')
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Marca")
        marcas = cursor.fetchall()
        cursor.execute("SELECT * FROM Categoria")
        categorias = cursor.fetchall()
        cursor.execute("SELECT * FROM Receta")
        recetas = cursor.fetchall()
        cursor.execute("SELECT * FROM Distribuidor")
        distribuidores = cursor.fetchall()
        return render_template('agregar_producto.html', marcas=marcas, categorias=categorias, recetas=recetas, distribuidores=distribuidores)

# Ruta para eliminar un producto
@app.route('/eliminar_producto/<int:id>', methods=['POST'])
def eliminar_producto(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM Producto WHERE ID_producto = %s", (id,))
    db.commit()
    return redirect('/productos')

# ruta para agregar cantidad al inventario
@app.route('/agregar_cantidad', methods=['GET', 'POST'])
def agregar_cantidad():
    if request.method == 'POST':
        producto_id = int(request.form['producto'])
        proveedor_id = int(request.form['proveedor'])
        id_sucursal = int(request.form['id_sucursal'])
        cantidad = int(request.form['cantidad'])

        cursor = db.cursor()
        cursor.execute("INSERT INTO Inventario (producto_id, proveedor_id, id_sucursal, cantidad) VALUES (%s, %s, %s, %s)",
                       (producto_id, proveedor_id, id_sucursal, cantidad))
        db.commit()
        return redirect('/productos')
    else:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Producto")
        productos = cursor.fetchall()
        cursor.execute("SELECT * FROM Proveedor")
        proveedores = cursor.fetchall()
        cursor.execute("SELECT * FROM Sucursal")
        sucursales = cursor.fetchall()
        return render_template('inventario.html', productos=productos, proveedores=proveedores, sucursales=sucursales)


#CLiente
################################################################
@app.route('/clientes')
def clienteView():
    # Obtenemos la lista de empleados
    data = listaClientes()
    return render_template('clientes.html', lista=data)

# Crear un nuevo cliente en la tabla "Cliente"
@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']
    id_sucursal = request.form['sucursal']
    crear_cliente(nombre, apellido, direccion, telefono, email, id_sucursal)
    return redirect(url_for('clienteView'))

# Eliminar un cliente de la tabla "Cliente" por su ID
@app.route('/delete_cliente/<string:id>',methods=['GET'] )
def delete_cliente(id):
    eliminar_cliente(id)
    return redirect(url_for('clienteView'))

# Actualizar los datos de un cliente en la tabla "Cliente"
@app.route('/edit_cliente/<string:id>')
def edit_cliente(id):
    cliente = obtener_cliente(id)
    return render_template('edit-cliente.html', cliente=cliente)

# Actualizar los datos de un cliente en la tabla "Cliente"
@app.route('/update_cliente/<string:id>', methods=['POST'])
def update_cliente(id):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']
    id_sucursal = request.form['sucursal']
    actualizar_cliente(id, nombre, apellido, direccion, telefono, email, id_sucursal)
    return redirect(url_for('clienteView'))

#Categoria
################################################################
@app.route('/categoria', methods=['GET', 'POST'])
def categoriaView():
    # Obtenemos la lista de categorías
    return render_template('categorias.html', lista=listaCategorias())

@app.route('/add_Categoria', methods=['POST'])
def add_Categoria():
    nombre = request.form['nombre']
    registrarCategoria(nombre)
    return redirect(url_for('categoriaView'))

@app.route('/delete_categoria/<string:id>')
def delete_categoria(id):
    eliminarCategoria(id)
    return redirect(url_for('categoriaView'))

@app.route('/edit_categoria/<string:id>', methods=['GET', 'POST'])
def edit_categoria(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        updateCategoria(nombre, id)
        return redirect(url_for('categoriaView'))
    else:
        return render_template('edit-categoria.html', data=getCategoria(id))




if __name__ == '__main__':
    app.run(debug=True)
