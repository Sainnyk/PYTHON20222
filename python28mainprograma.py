import python28anyobisiestoynumnarcisista
import datetime

#------------ PROGRAMA PRINCIPAL ----------------

python28anyobisiestoynumnarcisista.menu()
seleccion=int(input())

if(seleccion == 1):
    print("Introduzca un numero: ")
    numero = int(input())
    respuesta = python28anyobisiestoynumnarcisista.isBisiesto(numero)
    if(respuesta == True):
        print("El numero "+ str(numero) + " es bisiesto." )
    else:
        print("El numero "+ str(numero) + " NO es bisiesto." )

elif(seleccion == 2):
    print("Introduzca un numero: ")
    numero = input()
    respuesta= python28anyobisiestoynumnarcisista.isNarcisista(numero)
    if(respuesta == True):
        print("El numero "+ str(numero) + " es narcisista." )
    else:
        print("El numero "+ str(numero) + " NO es narcisista." )

elif(seleccion == 3):
    print("Introduzca año de nacimiento: ")
    anyoNacimiento = int(input())
    fechaActual = datetime.date.today()
    anyoActual = fechaActual.year
    for i in range(anyoNacimiento,anyoActual+1):
        if(python28anyobisiestoynumnarcisista.isBisiesto(int(i))):
            print(i)

elif(seleccion == 4):
    python28anyobisiestoynumnarcisista.print("¡Hasta luego!")


print("Pulse una tecla para cerrar....")
input()