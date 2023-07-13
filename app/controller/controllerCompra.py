from conexionBD import connectionBD

def ubicar_compras_por_fecha(fecha):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Compra_cliente WHERE fecha = %s"
    val = (fecha,)

    cursor.execute(querySQL, val)
    resultadoBusqueda = cursor.fetchall()

    cursor.close()
    conexion_MySQLdb.close()

    return resultadoBusqueda


def buscar_compras(fecha):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    if fecha:
        querySQL = "SELECT * FROM Compra_cliente WHERE fecha = %s"
        cursor.execute(querySQL, (fecha,))
    else:
        querySQL = "SELECT * FROM Compra_cliente"
        cursor.execute(querySQL)

    resultadoBusqueda = cursor.fetchall()
    cursor.close()
    conexion_MySQLdb.close()

    return resultadoBusqueda
