import pyodbc

print("Consulta SELECT con Python")

#Estos datos no son necesarios, pero por comodidad
servidor="LOCALHOST\SQLEXPRESS"
bbdd="HOSPITAL"
usuario="SA"
password="" #Como estamos tarbajando on premise no se pone (?)

#CREAMOS NUESTRA CADENA DE CONEXION
connectionString = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + "; PWD=" + password)
#Habria que poner un try y un catch, ahora para no marear no lo pondremos

#CONECTAMOS CON NUESTRA BBDD
print("Intentando conectar...")
conexion = pyodbc.connect(connectionString)
print("Conectado a SQL Server")

#TENEMOS UNA CONEXION ABIERTA, PODEMOS REALIZAR CONSULTAS
#CREAMOS UN CURSOR PARA REALIZAR UNA CONSULTA
cursor = conexion.cursor()
#El cursor maneja tanto consultas de seleccion como consultas de accion, le es indiferente

#CREAMOS NUESTRA CONSULTA SELECT -> Se guardan en variables normalmente llamadas "sql"
sql = "select * from DEPT" #es indiferente en mayus o minus, porque estamos directamente atacando sql, como lo hariamos desde la otra app
#sql = "select dept_no, dnombre, loc from DEPT" #al poner loc en minuscula, abajo, en el print(row.loc) podriamos ponerlo en minuscula, pero como esta en mayus en la BBDD hay que ponerlo en mayus
#El cursor es el encargado de ejecutar la consulta
cursor.execute(sql)

#TENEMOS DATOS DE LOS DEPARTAMENTOS, PODEMOS LEER FILA A FILA CADA UNO DE LOS DATOS CON EL METODO "fetchone()". DICHO METODO CADA VEZ QUE SE EJECUTA, SE MUEVE UNA FILA EN EL CURSOR
#fetchone SOLO imprime una fila cada vez. Si queremos pasar a la siguiente fila debemos repetir tanto el fetchone() como el print.
# row = cursor.fetchone()
# #DIBUJAMOS LA FILA ACTUAL
# print(row)

#VEMOS LAS SIGUIENTES FILAS
# row = cursor.fetchone()
# print(row)
# row = cursor.fetchone()
# print(row)
# row = cursor.fetchone()
# print(row)
# row = cursor.fetchone()
# print(row)
# row = cursor.fetchone()
# print(row)
# row = cursor.fetchone()
# print(row)

#PONER ESTO DE ARRIBA ES MUY ORTOPEDICO, MEJOR RECORRER LOS DATOS COMO UNA LISTA USANDO BUCLES
#******LOS NOMBRES DE COLUMNA SON CASE SENSITIVE*******
# for row in cursor:
#     #PODEMOS DIBUJAR POR EL INDICE DE LA COLUMNA EMPEZANDO EN 0
#     #EN ESTE CASO DIBUJAMOS POR POSICION, QUE CORRESPONDE A LA COLUMNA
#     print(row[1])
#     #TAMBIEN PODEMOS DIBUJAR CON EL NOMBRE DE LA COLUMNA DE MANERA DINAMICA
#     print(row.LOC)

# #UN CURSOR SOLO SE LEE UNA VEZ. SI NECESITAMOS LEER LOS DATOS DE NUEVO, TENDRIAMOS QUE EJECUTAR LA CONSULTA DE NUEVO
# row = cursor.fetchone()
# #DEBEMOS CERRAR EL CURSOR DESPUES DE USARLO
# cursor.close()

#SE PUEDEN GUARDAR LOS DATOS EN VARIABLES
# for row in cursor:
#     numero = row.DEPT_NO
#     nombre = row.DNOMBRE
#     localidad = row.LOC
#     print(str(numero) + ", Nombre: "+nombre+", Localidad: "+ localidad)

#SE PUEDE ASIGNAR AUTOMATICAMENTE LOS DATOS CON LAS VARIABLES. Si el select * tiene 3 elementos, se ponen 3 variables, si vienen 5, se ponen 5.
for numero, nombre, localidad in cursor:
    print(str(numero) + ", Nombre: "+nombre+", Localidad: "+ localidad)

cursor.close()
# #CERRAMOS LA CONEXION
conexion.close()