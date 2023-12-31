from conexionBD import connectionBD

def obtener_producto_por_id(id_producto):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM Producto WHERE ID_producto = %s"
    cursor.execute(querySQL, (id_producto,))
    producto = cursor.fetchone()

    cursor.close()
    conexion_MySQLdb.close()

    return producto

def obtener_productos():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "SELECT * FROM Producto"
    cursor.execute(querySQL)

    productos = cursor.fetchall()

    cursor.close()
    conexion_MySQLdb.close()

    return productos

