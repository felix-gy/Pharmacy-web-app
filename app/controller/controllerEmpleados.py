from conexionBD import connectionBD
import random

def listaEmpleados():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Empleado"

    cursor.execute(querySQL)
    resultadoBusqueda = cursor.fetchall()
    totalBusqueda = len(resultadoBusqueda)
    cursor.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda


def registrarEmpleado(nombre='', apellido='', direccion='', telefono='', email='', contrato_fecha='', id_sucursal=''):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    # Generar un ID aleatorio de 10 dígitos
    id_empleado = str(random.randint(10, 100))

    sql = "INSERT INTO Empleado (ID_empleado, nombre, apellido, direccion, telefono, email, contrato_fecha, ID_sucursal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (id_empleado, nombre, apellido, direccion, telefono, email, contrato_fecha, id_sucursal)

    cursor.execute(sql, valores)
    conexion_MySQLdb.commit()
    cursor.close()
    conexion_MySQLdb.close()

    resultado_insert = cursor.rowcount
    ultimo_id = cursor.lastrowid
    return resultado_insert

def obtenerEmpleadoPorCorreo(correo):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Empleado WHERE email = %s"
    valor = (correo,)

    cursor.execute(querySQL, valor)
    empleados = cursor.fetchall()

    cursor.close()
    conexion_MySQLdb.close()

    if empleados:
        return empleados[0]
    else:
        return None
    
def obtenerEmpleadoPorID(id_empleado):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Empleado WHERE ID_empleado = %s"
    valores = (id_empleado,)

    cursor.execute(querySQL, valores)
    empleado = cursor.fetchone()

    cursor.close()
    conexion_MySQLdb.close()

    return empleado

def actualizarEmpleado(id_empleado, nombre, apellido, direccion, telefono, email, id_sucursal):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "UPDATE Empleado SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, email = %s, ID_sucursal = %s WHERE ID_empleado = %s"
    valores = (nombre, apellido, direccion, telefono, email, id_sucursal, id_empleado)

    cursor.execute(querySQL, valores)
    conexion_MySQLdb.commit()

    cursor.close()
    conexion_MySQLdb.close()

def eliminarEmpleado(id_empleado):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    # Consulta SQL para eliminar al empleado por su ID
    sql = "DELETE FROM Empleado WHERE ID_empleado = %s"
    valor = (id_empleado,)

    cursor.execute(sql, valor)
    conexion_MySQLdb.commit()

    cursor.close()
    conexion_MySQLdb.close()

def obtenerVentasRealizadasPorEmpleado(id_empleado):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Venta_empleado WHERE ID_empleado = %s"
    cursor.execute(querySQL, (id_empleado,))
    ventas = cursor.fetchall()
    cursor.close()
    conexion_MySQLdb.close()

    return ventas
