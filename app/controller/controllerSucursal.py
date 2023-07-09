from conexionBD import *  #Importando conexion BD

def listaSucursales():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cursor      = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM Sucursal"
    cursor.execute(querySQL) 
    resultadoBusqueda = cursor.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    cursor.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return resultadoBusqueda

def registrarSucursal( nombre='',direccion='',telefono = ''):       
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)

        sql = ("INSERT INTO Sucursal(direccion, telefono, nombre, ID_farmacia) VALUES (%s, %s, %s, %s)")
        valores = (direccion, telefono, nombre, 1)
        
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        # resultado_insert = cursor.rowcount #retorna 1 o 0
        # ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        # return resultado_insert

def eliminarSucursal(id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    cursor.execute("DELETE FROM Sucursal WHERE ID_sucursal = %s", (id,))
    conexion_MySQLdb.commit()
    cursor.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD

def getSucursal(id):
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Sucursal WHERE ID_sucursal = %s LIMIT 1", (id,))
    resultadoBusqueda = cursor.fetchone()
    cursor.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD
    return resultadoBusqueda

def updateSucursal(nombre,direccion,telefono,id):       
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    cursor.execute("""
        UPDATE Sucursal
        SET nombre = %s,
            direccion = %s,
            telefono = %s
        WHERE ID_sucursal = %s
    """, (nombre, direccion, telefono, id))
    conexion_MySQLdb.commit()
    cursor.close() #cerrando conexion de la consulta sql
    conexion_MySQLdb.close() #cerrando conexion de la BD
    #resultado_update = cursor.rowcount #retorna 1 o 0