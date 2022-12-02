def menu():
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividr")
    print("4.- Multiplicar")

def sumar(numero1,numero2):
    suma = numero1 + numero2
    print(str(numero1) + " + " + str(numero2) + " = " + str(suma))

def restar(numero1,numero2):
    resta = numero1 - numero2
    print(str(numero1) + " - " + str(numero2) + " = " + str(resta))

def dividir(numero1,numero2):
    division = numero1 / numero2
    print(str(numero1) + " / " + str(numero2) + " = " + str(int(division)))

def multiplicar(numero1,numero2):
    mult = numero1 * numero2
    print(str(numero1) + " * " + str(numero2) + " = " + str(mult))
#------- PROGRAMA PRINCIPAL--------------

respuesta = "s"
opcion = 5

while(opcion != 0):
    if(respuesta == "s"):
        print("Introduzca un numero: ")
        numero1 = int(input())
        print("Introduzca otro numero: ")
        numero2 = int(input())

    print("Seleccione una opcion: ")
    menu()
    opcion = int(input())

    if(opcion == 0):
        print("¡Hasta luego!")
    elif(opcion == 1):
        sumar(numero1, numero2)
    elif(opcion == 2):
        restar(numero1, numero2)
    elif(opcion == 3):
        dividir(numero1, numero2)
    elif(opcion == 4):
         multiplicar(numero1, numero2)
        
    print("¿Desea poner numeros diferentes? (s/n)")
    respuesta = input()



