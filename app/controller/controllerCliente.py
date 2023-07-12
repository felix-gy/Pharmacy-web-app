from conexionBD import *  #Importando conexion BD

def listaClientes():
    conexion = connectionBD()
    cursor = conexion.cursor(dictionary=True)
    sql = "SELECT * FROM Cliente"
    cursor.execute(sql)
    Busquedaclientes = cursor.fetchall()
    cursor.close()
    return Busquedaclientes

# Crear un nuevo cliente en la tabla "Cliente"
def crear_cliente(nombre, apellido, direccion, telefono, email, id_sucursal):
    conexion = connectionBD()
    cursor = conexion.cursor()
    sql = "INSERT INTO Cliente (nombre, apellido, direccion, telefono, email, ID_sucursal) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (nombre, apellido, direccion, telefono, email, id_sucursal)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

# Obtener un cliente de la tabla "Cliente" por su ID
def obtener_cliente(id_cliente):
    conexion = connectionBD()
    cursor = conexion.cursor(dictionary=True)
    sql = "SELECT * FROM Cliente WHERE ID_cliente = %s"
    valores = (id_cliente,)
    cursor.execute(sql, valores)
    cliente = cursor.fetchone()
    cursor.close()
    return cliente

# Actualizar los datos de un cliente en la tabla "Cliente"
def actualizar_cliente(id_cliente, nombre, apellido, direccion, telefono, email, id_sucursal):
    conexion = connectionBD()
    cursor = conexion.cursor()
    sql = "UPDATE Cliente SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, email = %s, ID_sucursal = %s WHERE ID_cliente = %s"
    valores = (nombre, apellido, direccion, telefono, email, id_sucursal, id_cliente)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

# Eliminar un cliente de la tabla "Cliente" por su ID
def eliminar_cliente(id_cliente):
    conexion = connectionBD()
    cursor = conexion.cursor()
    sql = "DELETE FROM Cliente WHERE ID_cliente = %s"
    valores = (id_cliente,)
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()

def obtener_ultimo_id_cliente():
    conexion_MySQLdb = connectionBD()
    cursor = conexion_MySQLdb.cursor()

    querySQL = "SELECT MAX(ID_cliente) FROM Cliente"
    cursor.execute(querySQL)

    ultimo_id_cliente = cursor.fetchone()[0]
    cursor.close()
    conexion_MySQLdb.close()

    if ultimo_id_cliente:
        return ultimo_id_cliente
    else:
        return 0