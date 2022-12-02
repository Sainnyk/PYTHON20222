def convertirMayusculas(texto):
    #Devolvemos el texto a mayusculas
    return texto.upper()

def convertirMinusculas(texto):
    return texto.lower()

def mostrarMenu():
    print("Selecciona una opcion: ")
    print("1.- Convertir en minusculas")
    print("2.- Convertir en mayusculas")
#--------PROGRAMA PRINCIPAL--------
print("Metodos RETURN")

print("Introduzca un texto")
valor = input()

mostrarMenu() #METODO DE ACCION
#Capturamos lo que el usuario ha escrito, 1 o 2
opcion = int(input())

if(opcion == 1):
    valor = convertirMinusculas(valor)
    print("Minusculas: " + valor)
else:
    valor = convertirMayusculas(valor)
    print("Mayusculas: " + valor)



