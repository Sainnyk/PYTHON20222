    # #Tenemos una lista de ciudades
# ciudades = ["Sevilla", "Oviedo", "Bilbao", "Alicante", "Cordoba", "Malaga"]

#     #Necesitamos almacenar la lista en un formato string para un fichero.
#     #Vamos a separar los elementos con JOIN indicando un caracter (@) en este caso
#     #       "caracter separador".join(lista)
# contenido = "@".join(ciudades)
# print(contenido)

#     #Para recuperar de un string una lista, se usa el metodo SPLIT
#     #       nombreLista = String.split(sep="CARACTER SEPARADOR")
# cities = contenido.split("@") #Devolver una lista separando el string por cadenas de @
# for ciudad in cities:
#     print(ciudad)

#---------------------EJEMPLO DE VERDAD----------------------
#DEclaramos coleccion para almacenar ciudades
ciudades=[]

def showCiudades():
    global ciudades
    for ciudad in ciudades:
        print(ciudad)
    
#METODO PARA LEER LAS CIUDADES
def readFile():
    fichero = open("ciudades.txt","r")
    contenido = fichero.read()
    fichero.close()
    #ALMACENAMOS EN CIUDADES LA INFORMACION RECUPERADA
    global ciudades #sin esto no estamos modificando la variable ciudad
    ciudades = contenido.split(sep="@")
    print("Datos cargados correctamente")
    print("Numero de ciudades: " + str(len(ciudades)))

#METODO PARA GUARDAS LAS CIUDADES EN UN FICHERO
def saveFile():
    #CONVERTIMOS LA LISTA A STRING CON UN SEPARADOR
    resultado = "@".join(ciudades)
    fichero = open("ciudades.txt","w+")
    fichero.write(resultado)
    fichero.flush()
    fichero.close()
    print("Datos almacenados correctamente")

#METODO PARA AÑADIR CIUDADES A LA COLECCION
def insertarCiudad():
    print("Introduzca nombre de ciudad")
    ciudad = input()
    ciudades.append(ciudad)

#---------PROGRAMA PRINCIPAL----------------------
print("Ejemplo ciudades y Files")
opcion = -1

while(opcion != 0):
    print("0.-Salir")
    print("1.- Leer File de ciudades")
    print("2.- Guardar File ciudades")
    print("3.- Nueva ciudad")
    print("4.- Mostrar ciudades")
    print("Seleccione una opcion")
    opcion = int(input())

    if (opcion == 1):
        readFile()
    elif (opcion == 2):
        saveFile()
    elif (opcion == 3):
        insertarCiudad()
    elif (opcion == 4):
        showCiudades()
    elif (opcion == 0):
        print("Hasta luego")
    else:
        print("Opcion incorrecta")