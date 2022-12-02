#COMENTAR: CONTROL + K + C
#DESCOMENTAR: CONTROL + K + U

print("Primer Python")

#Declaracion de variables
numero= 21

#Los tipos de dato String irán entre comillas dobles
texto= "Mi primer String en Python"

#print("El numero es: ", numero)
#print("El numero es: " + numero) #Este es el que vamos a usar (el +) 
#SOLO SE PUEDE CONTATENAR STRINGS, HAY QUE USAR FUNCIONES DE CONVERSION. EL PRINT DE ARRIBA DA ERROR POR CONCATENAR INT
print("Mi texto es: " + texto)

# FUNCIONES DE CONVERSION
#str(variable): convierte una variable a tipo String
#float(variable): convierte una variable a tipo decimal
#int(variable): convierte una variable a tipo entero

print("El numero es: " + str(numero))