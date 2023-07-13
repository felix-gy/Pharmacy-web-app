from conexionBD import *  #Importando conexion BD

def listaFarmacia():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM Farmacia"
    cursor.execute(querySQL)
    resultadoBusqueda = cursor.fetchall()
    cursor.close()
    conexion_MySQLdb.close()
    return resultadoBusqueda