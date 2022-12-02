from math import *

def menu():
    print("Escoja una opcion: ")
    print("1.- Bisiesto")
    print("2.- Narcisista")
    print("3.- Años bisiestos año nacimiento")
    print("4.- Salir")

def isBisiesto(numero):

    if(numero % 4 == 0):
        if((numero % 100 == 0 and numero % 400 == 0) or (numero % 100 != 0)):
                return True
        else:
            return False
    else:
        return False


def isNarcisista(numero):

    suma = 0
    longitud= len(numero)
    
    for i in range (longitud):
        caracter = numero[i]
        cifra = int(caracter)
        potencia = pow(cifra,longitud)
        suma = suma + potencia

    if(int(numero) == int(suma)):
        return True
    else:
        return False

