import mysql.connector

#Conectandose la base desplegada en la nube
#NUEVA CONEXION:
def connectionBD():
    mydb = mysql.connector.connect(
        host ="sql.freedb.tech",
        user ="freedb_db_pharmacy_222",
        passwd ="sT$w&z&Btw6CsJw",
        database = "freedb_admin_test_1"
        )
    if mydb:
        print ("Conexion exitosa a BD")
        return mydb
    else:
        print("Error en la conexion a BD")
