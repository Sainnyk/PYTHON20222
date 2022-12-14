from class45conexionenfermos import ConexionEnfermos

#CREAMOS UN OBJETO DE LA CLASE CONEXIONENFERMOS
connection = ConexionEnfermos() #automaticamente ya se ha conectado a la base de datos

print("Inserte una inscripcion para eliminar: ")
inscripcion = input()
#EL METODO ELIMINAR DEVUELVE EL NUMERO DE ENFERMOS ELIMINADOS
respuesta = connection.eliminarEnfermo(inscripcion)

print("Enfermos eliminados: "+str(respuesta))