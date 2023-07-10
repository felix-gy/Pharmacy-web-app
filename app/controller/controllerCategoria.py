from conexionBD import *  #Importando conexion BD
def listaCategoria():
    conexion = connectionBD()
    cursor = conexion.cursor(dictionary=True)
    sql = "SELECT * FROM Categoria"
    cursor.execute(sql)
    Busquedaclientes = cursor.fetchall()
    cursor.close()
    return Busquedaclientes

def eliminar_categoria(id_categoria):
    conexion = connectionBD()
    cursor = conexion.cursor()
    
    sql = "DELETE FROM Categoria WHERE ID_categoria = %s"
    valores = (id_categoria,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

def crear_categoria(nombre):
    conexion = connectionBD()
    cursor = conexion.cursor()
    sql = "INSERT INTO Categoria (nombre) VALUES (%s)"
    valores = (nombre,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()