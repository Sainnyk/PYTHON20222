import pyodbc

print("INSERTAR DEPARTAMENTO")

servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = ""

connectionString = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER="+servidor+"; DATABASE="+bbdd+"; UID="+usuario+"; PWD="+ password

conexion = pyodbc.connect(connectionString)
print("Conectado")

#VAMOS A PEDIR LOS DATOS AL USUARIO Y LOS USAREMOS PARA CONCATENAR Y REALIZAR NUESTRA CONSULTA INSERT
print("Introduzca un numero: ")
numero = input()
print("Introduzca nombre de departamento: ")
nombre = input()
print("Introduzca localidad: ")
localidad = input()

sql = "insert into DEPT values (" + numero + ",'" + nombre +"','"+localidad+ "')"
#print sql -> Para ver si he concatenado bien los datos

#DECLARAMOS NUESTRO CURSOR
cursor = conexion.cursor()
#Ejecutamos la consulta SOBRE EL CURSOR
cursor.execute(sql)

#Para averiguar el numero de registros que han sido afectados por la consulta, se usa la propiedad rowcount del cursor (devuelve un numero)
filasInsertadas = cursor.rowcount
print("Rowcount: " + str(filasInsertadas))

#En python, las consultas de accion se realizan de forma temporal, es decir, no son llevadas a la BBDD hasta que no se lo decimos explicitamente mediante el método "commit" del cursor
cursor.commit()
#cursor.rollback() Indicamos que deshaga los cambios
cursor.close()

#LOS CURSORES SE PUEDEN REUTILIZAR PARA DIFERENTES CONSULTAS (AL IGUAL QUE LA VARIABLE SQL).
#VAMOS A REUTILIZAR ESTA MISMA VARIABLE A CONTINUACION PARA UNA CONSULTA DE SELECCION. COMO NECESITAMOS LA CONEXION ABIERTA, NO LA CERRAMOS, SOLO EL CURSOR.
sqlselect = "SELECT * FROM DEPT"
cursor = conexion.cursor()
cursor.execute(sqlselect)
print("-------------------DEPARTAMENTOS-------------------------")
for row in cursor:
    print(row.DNOMBRE +", "+row.LOC)

cursor.close() #SI NO SE CIERRA SE RELANTIZA TODO EN UNA BBDD GRANDE DE VERDAD

conexion.close()