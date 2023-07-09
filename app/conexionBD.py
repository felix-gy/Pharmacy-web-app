#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

#Conectandose la base desplegada en la nube
def connectionBD():
    mydb = mysql.connector.connect(
        host ="127.0.0.1",
        user ="root",
        passwd ="gordillo303132x",
        database = "db_pharmacy"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")

# def connectionBD():
#     mydb = mysql.connector.connect(
#         host ="sql.freedb.tech",
#         user ="freedb_db_test_111",
#         passwd ="4JKtwGf@DQD@b?w",
#         database = "freedb_db_pharmacy"
#         )
#     if mydb:
#         print ("Conexion exitosa a BD")
#         return mydb
#     else:
#         print("Error en la conexion a BD")