def menu():
    print("0.- Salir")
    print("1.- Nuevo nombre")
    print("2.- Eliminar nombre")
    print("3.- Comenzar de nuevo")
    print("Seleccione una opcion")

def anyadirNombre(nombre):
    lista.append(nombre)

def eliminarNombre(indice):
    lista.pop(indice)

def comenzar():
    lista.clear()
    
def mostrarLista(lista):
    print("Lista de nombres introducidos: ")
    for i in range(len(lista)):
        name = lista[i]
        print(str(i)+ ".-" + name)
    print("-------------------------------------------")


#-------PRGRAMA PRINCIPAL-------

nombre = ""
lista=[]
seleccion = 1
while(nombre != "OK"):
    print("Introduzca un nombre o escriba OK para continuar")
    nombre = input()
    lista.append(nombre)
    print("Datos almenacados: " + str(len(lista)))

mostrarLista(lista)
menu()
seleccion = int(input())
if(seleccion == 0):
    print("¡Hasta luego!")
elif(seleccion == 1 ):
    print("¿Qué nombre desea anydir?")
    name = input()
    anyadirNombre(name)
    mostrarLista(lista)
elif(seleccion == 2 ):
    print("¿Qué posicion desea eliminar?")
    try:
        indice = int(input())
        eliminarNombre(indice)
    except IndexError:
        print("Ha introducido una posicion no valida")
    except ValueError:
        print("Debe introducir una opcion valida")
    finally:
        mostrarLista(lista)
elif(seleccion == 3 ):
    comenzar()
    mostrarLista(lista)