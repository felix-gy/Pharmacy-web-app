from conexionBD import *  #Importando conexion BD

def listaCategorias():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM Categoria"
    cursor.execute(querySQL)
    resultadoBusqueda = cursor.fetchall()
    cursor.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda

def registrarCategoria(nombre):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    sql = "INSERT INTO Categoria(nombre) VALUES (%s)"
    valores = (nombre,)
    cursor.execute(sql, valores)
    conexion_MySQLdb.commit()
    cursor.close()
    conexion_MySQLdb.close()

def eliminarCategoria(id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    cursor.execute("DELETE FROM Categoria WHERE ID_categoria = %s", (id,))
    conexion_MySQLdb.commit()
    cursor.close()
    conexion_MySQLdb.close()

def getCategoria(id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Categoria WHERE ID_categoria = %s LIMIT 1", (id,))
    resultadoBusqueda = cursor.fetchone()
    cursor.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda

def updateCategoria(nombre, id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    cursor.execute("UPDATE Categoria SET nombre = %s WHERE ID_categoria = %s", (nombre, id))
    conexion_MySQLdb.commit()
    cursor.close()
    conexion_MySQLdb.close()
