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
    database=creds[2],
    passwd=creds[3]
)
cursor = conn.cursor(dictionary=True)

# Obtener todos los datos de la tabla de familia
cursor.execute("SELECT id,principal FROM familia")
familias = cursor.fetchall()

print("Ejecutando...")
i=0
# Iterar sobre los datos de ambas tablas
for familia in familias:
    i+=1
    cursor.execute("SELECT familia FROM socio WHERE id=%s",(familia["principal"],))
    socio = cursor.fetchall()[0]
    if(socio["familia"]!=familia["id"]):
        print("Error en familia "+str(familia["id"]))

print("Ejecutado con "+str(i)+" errores")
# Cerrar la conexión a la base de datos
conn.close()