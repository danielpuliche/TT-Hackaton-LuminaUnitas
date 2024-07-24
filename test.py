import pyodbc
import pandas as pd

server = 'luminitas-server.database.windows.net'
database = 'denunciasDB'
username = 'admin-luminitas'
password = 'lumun-12345'
driver= '{ODBC Driver 17 for SQL Server}'

try:
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
except:
    print("Error con la conexión")

cursor = conn.cursor()

try:
    cursor.execute(
        "INSERT INTO your_table VALUES (5,'vasd',3,6.4);"
    )

    cursor.execute(
        "SELECT * FROM your_table;"
    )

    datos = cursor.fetchall()

    for dato in datos:
        print(dato)

except:
    print("Error consulta")

try:
    cursor.commit()
    cursor.close()
    conn.close()
except:
    print("Fallo cierre de conexión")