#--------METODOS CLASE STRING-------------------

texto = "primero python"

#Metodos
print("Upper: " + texto.upper())
print("Replace o-@: " + texto.replace("o","@"))
print("texto[0]: " + texto[0])
print("Longitud len(): " + str(len(texto)))
print("find letra P: " + str(texto.find("P")))
print("find letra p: " + str(texto.find("p")))

#SOBRECARGA - POLIMORFISMO - find
print("find sobrecarga p, desde posicion 1: " + str(texto.find("p",1)))

#Las posiciones (indices) no cambian, solamente cambia si buscamos desde el inicio del texto o del final
print("rfind buscar letra p (desde el final): " + str(texto.rfind("p")))
print("startswith A: " + str(texto.startswith("A")))
print("endswith n: " + str(texto.endswith("n")))
print("isdigit(): " + str(texto.isdigit()))
print("isalpha(): " + str(texto.isalpha()))
print("isalnum(): " + str(texto.isalnum()))

#Slicing, substring
#Queremos mostrar de la posicion 2 en adelante
subcadena = texto[2:]
print("Posicion 2 en adelante: " + subcadena)
#Desde una posicion hasta otra
subcadena = texto[2:5] #DE INDICE 2 A INDICE 5
print("Posicion del 2 al 5: " + subcadena)

#Recorrer todos los caracteres de la cadena uno a uno
longitud = len(texto)
for i in range(longitud): #longitud es = 14, asi que el rango sera 14-1 e "i" llegará hasta el indice 13 empezando por 0
    letra = texto[i]
    print(str(i) + " : " + letra)

#Si deseamos pedir un numero al usuario y saber si es un numero o no, el truco esta en almacenar en una variable string el valor que nos ha dado el usuario
print("Introduzca un numero: ")
aux = input()
if(aux.isdigit()):
    print("ES UN NUMERO")
else:
    print("NO ES UN NUMERO")