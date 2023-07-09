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
