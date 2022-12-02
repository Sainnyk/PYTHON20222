#ESTA CLASE NO SE EJECUTA, SE USA EN OTRAS CLASES

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