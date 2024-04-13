import mysql.connector

def read_file(file):
    with open(file, 'r') as archivo:
        valor=[]
        for linea in archivo:
            valor.append(linea.strip())
        return valor

creds=read_file("bbdd.txt")

# Conectar a la base de datos
conn = mysql.connector.connect(
    host=creds[0],
    user=creds[1],
    database=creds[2]
)
cursor = conn.cursor(dictionary=True)

# Obtener todos los datos de la primera tabla
cursor.execute("SELECT id,principal FROM familia")
familias = cursor.fetchall()



# Iterar sobre los datos de ambas tablas
for familia in familias:
    # Aquí puedes hacer lo que quieras con los datos de ambas tablas
    # Obtener todos los datos de la segunda tabla
    cursor.execute("SELECT familia FROM socio WHERE id=%s",(familia["principal"],))
    socio = cursor.fetchall()[0]
    if(socio["familia"]!=familia["id"]):
        print("Error en familia "+str(familia["id"]))

# Cerrar la conexión a la base de datos
conn.close()