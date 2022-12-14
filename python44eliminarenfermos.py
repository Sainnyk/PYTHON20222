import pyodbc

servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="" 

#CREAMOS NUESTRA CADENA DE CONEXION
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

conexion =  pyodbc.connect(connectionString)
print("CONECTADO")


sql = "SELECT INSCRIPCION, APELLIDO FROM ENFERMO"

cursor = conexion.cursor()
cursor.execute(sql)

print("----------------------LISTADO DE ENFERMOS----------------------------")
for row in cursor:
    print("INSCRIPCION: " + row.INSCRIPCION + ", APELLIDO: "+ row.APELLIDO)

print("Inserte el nº de inscripcion para eliminar un enfermo: ")
inscripcion = input()

sql = "DELETE FROM ENFERMO WHERE INSCRIPCION =?"
cursor.execute(sql,(inscripcion))

affectedData = cursor.rowcount

print("Registro eliminado: " + str(affectedData))

print("----------------------NUEVO LISTADO----------------------------")
sql = "SELECT INSCRIPCION, APELLIDO FROM ENFERMO"
cursor.execute(sql)

for row in cursor:
    print("INSCRIPCION: " + row.INSCRIPCION + ", APELLIDO: "+ row.APELLIDO)

cursor.close()
conexion.close()