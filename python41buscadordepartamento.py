import pyodbc

print("Buscador departamentos")

servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="" 

#CREAMOS NUESTRA CADENA DE CONEXION
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
#Habria que poner un try y un catch, ahora para no marear no lo pondremos

#CONECTAMOS CON NUESTRA BBDD
print("Intentando conectar...")
conexion = pyodbc.connect(connectionString)
print("Conectado a SQL Server")

#PEDIMOS UN NUMERO DE DEPARTAMENTO AL USUARIO
print("Introduzca un numero de departamento")
#EL USUARIO NOS DARA UN NUMERO, QUE USAREMOS PARA CONCATNAR A LA CONSULTA POR LO QUE, AUNQUE SEA UN NUMERO, ES UN DATO STRING (NO LO QUIERO PARA SUMAR NI PARA NADA DE ESO)
data = input()
sql = "select * from DEPT where DEPT_no="+ data
#SOLAMENTE DEVOLVERA UNA FILLA, YA QUE BUSCAMOS POR EL ID. COMO SOLO ES UNA USAMOS FETCHONE()
cursor = conexion.execute(sql) #extrae el resultado de la consulta y la guarda en cursor

row = cursor.fetchone()

#PARA PREGUNTAR SI TENEMOS DATOS O NO EN LA FILA SE USA EL OPERADOR NOT
if (not row):
    print("No existe el departamento "+ data)
else:
    print(row.DNOMBRE + ", "+ row.LOC)

cursor.close()
conexion.close()