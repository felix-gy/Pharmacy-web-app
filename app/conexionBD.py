import mysql.connector

#Conectandose la base desplegada en la nube
#NUEVA CONEXION:

#########################################################
#COLOCA TU SERVER LOCAL AQUI Y EN EL APP:PY
def connectionBD():
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database = ""
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")
