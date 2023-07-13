from conexionBD import connectionBD

def listaProductos():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Producto"

    cursor.execute(querySQL)
    resultadoBusqueda = cursor.fetchall()
    totalBusqueda = len(resultadoBusqueda)
    cursor.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda

def listaVentas():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Venta_empleado"

    cursor.execute(querySQL)
    resultadoBusqueda = cursor.fetchall()
    totalBusqueda = len(resultadoBusqueda)
    cursor.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda

def listaCompras():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Compra_cliente"

    cursor.execute(querySQL)
    resultadoBusqueda = cursor.fetchall()
    totalBusqueda = len(resultadoBusqueda)
    cursor.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda

def crearTransaccion(tipo, cantidad, id_venta, id_compra, id_factura):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "INSERT INTO Transaccion_compra_venta (tipo, cantidad, ID_venta, ID_compra, ID_factura) VALUES (%s, %s, %s, %s, %s)"
    val = (tipo, cantidad, id_venta, id_compra, id_factura)

    cursor.execute(querySQL, val)

    conexion_MySQLdb.commit()
    cursor.close()
    conexion_MySQLdb.close()

def obtener_venta_por_id(id_venta):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    # Consulta SQL para obtener la venta por su ID
    querySQL = "SELECT * FROM Venta_empleado WHERE ID_venta = %s"

    # Ejecutar la consulta SQL con el ID de venta proporcionado
    cursor.execute(querySQL, (id_venta,))
    resultadoVenta = cursor.fetchone()

    # Cerrar el cursor y cerrar la conexión a la base de datos
    cursor.close()
    conexion_MySQLdb.close()

    # Retornar el resultado de la consulta
    return resultadoVenta

def obtener_compra_por_id(id_compra):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    # Consulta SQL para obtener la compra por su ID
    querySQL = "SELECT * FROM Compra_cliente WHERE ID_compra = %s"

    # Ejecutar la consulta SQL con el ID de compra proporcionado
    cursor.execute(querySQL, (id_compra,))
    resultadoCompra = cursor.fetchone()

    # Cerrar el cursor y cerrar la conexión a la base de datos
    cursor.close()
    conexion_MySQLdb.close()

    # Retornar el resultado de la consulta
    return resultadoCompra

def insertar_venta_empleado(id_venta, fecha_actual, total_venta, id_empleado, id_producto):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "INSERT INTO Venta_empleado (ID_venta, fecha, total, ID_empleado, ID_producto) VALUES (%s, %s, %s, %s, %s)"
    val = (id_venta, fecha_actual, total_venta, id_empleado, id_producto)

    cursor.execute(querySQL, val)
    conexion_MySQLdb.commit()

    cursor.close()
    conexion_MySQLdb.close()

def insertar_compra_cliente(id_compra, fecha, total, id_cliente, id_producto):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "INSERT INTO Compra_cliente (ID_compra, fecha, total, ID_cliente, ID_producto) VALUES (%s, %s, %s, %s, %s)"
    val = (id_compra, fecha, total, id_cliente, id_producto)

    cursor.execute(querySQL, val)
    conexion_MySQLdb.commit()

    cursor.close()
    conexion_MySQLdb.close()


def generar_factura(id_venta, id_compra, id_factura):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "INSERT INTO Factura (ID_factura, ID_venta, ID_compra) VALUES (%s, %s, %s)"
    val = (id_factura, id_venta, id_compra)

    cursor.execute(querySQL, val)
    conexion_MySQLdb.commit()

    cursor.close()
    conexion_MySQLdb.close()

def insertar_factura(id_factura, fecha, total, id_cliente):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "INSERT INTO Factura (ID_factura, fecha, total, ID_cliente) VALUES (%s, %s, %s, %s)"
    val = (id_factura, fecha, total, id_cliente)

    cursor.execute(querySQL, val)
    conexion_MySQLdb.commit()

    cursor.close()
    conexion_MySQLdb.close()

import random

def obtener_factura_por_id(id_factura):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    # Generar un ID de factura aleatorio entre 1000 y 10000
    id_factura_aleatorio = random.randint(1000, 10000)

    querySQL = "SELECT * FROM Factura WHERE ID_factura = %s"
    val = (id_factura_aleatorio,)

    cursor.execute(querySQL, val)
    resultadoBusqueda = cursor.fetchone()

    cursor.close()
    conexion_MySQLdb.close()

    return resultadoBusqueda

def obtener_reporte_compras():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Compra_cliente"

    cursor.execute(querySQL)
    resultadoBusqueda = cursor.fetchall()

    cursor.close()
    conexion_MySQLdb.close()

    return resultadoBusqueda

