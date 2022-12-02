#from python25funcionesmatematicas import menu, restar
from python25funcionesmatematicas import *


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
