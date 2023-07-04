#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

#Conexion a la base de datos alojada en Railway 
def connectionBD():
    mydb = mysql.connector.connect(
        host ="containers-us-west-3.railway.app",
        user ="root",
        passwd ="WsyaOxtoAftnbyIB93Wv",
        database = "railway"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")
    