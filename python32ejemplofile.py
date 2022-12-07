print("EJEMPLO FICHEROS PYTHON")

# Creamos un nuevo archivo y escribimos algo en el
#Vamos a usar w+ (Lectura/Escritura) aunque w tambien serviria
fichero = open("nombre.txt","w+") #(nombre de archivo, tipo de acceso)
print("Introduzca su nombre")
nombre = input()
#Escribimos en el archivo
fichero.write("Su nombre es "+nombre)
# Es recomendable/obligatorio usar FLUSH
fichero.flush() #Con pocos datos puede funcionar sin este metodo, pero en muchos casos no guardara las cosas en el archivo
#Siempre cerramos el archivo para todas las acciones
fichero.close() #Normalmente se usa finally para esto

#Añadimos informacion al archivo creado. Lo abrimos en modo APPEND (a)
archivo = open("nombre.txt", "a") #no hace falta crear otra variable, podemos seguir usando "fichero", estamos fingiendo usar programas diferentes
print("Introduzca otro nombre")
nombre = input()
archivo.write("\n Nuevo nombre: "+nombre)
archivo.flush()
archivo.close()

#Por último, leemos el contenido de lo que hemos almacenado en el fichero en solo modo lectura
file = open("nombre.txt", "r")
contenido = file.read()
print("-------------------------------------")
print(contenido)
file.close()