import pyodbc

print("CAMBIAR SALARIO")

servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="" 

#CREAMOS NUESTRA CADENA DE CONEXION
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)

conexion = pyodbc.connect(connectionString)
print("Conectado")

print("Inserte un OFICIO: ")
oficio = input()
print("Inserte cuanto salario incrementar: ")
salario = input()

sql="UPDATE EMP SET SALARIO += ? WHERE OFICIO =?"

cursor = conexion.cursor()
cursor.execute(sql,(salario,oficio))
cursor.commit()
affectedData = cursor.rowcount
print("Empleados modificados:" + str(affectedData))

#AHORA GUARDAMOS EN CURSOR LA CONSULTA DONDE SELECCIONAMOS LOS DATOS AFECTADOS
sqlSelect = "SELECT APELLIDO,OFICIO, SALARIO FROM EMP WHERE OFICIO=?"
cursor.execute(sqlSelect,(oficio))

for row in cursor:
    print("APELLIDO: "+ row.APELLIDO +", OFICIO: "+ row.OFICIO+", SALARIO: "+ str(row.SALARIO))

cursor.close()
conexion.close()