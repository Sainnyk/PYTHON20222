import math

def menu():
    print("1.- Validar Mail")
    print("2.- Validar ISBN")
    print("3.- Mostrar letra DNI")
    print("4.- Salir")



def validarIsbn():
    print("Validacion numero ISBN de libros")

    print("Introduzca el ISBN a validar: ")
    isbn = input()


    while((isbn.isdigit() == False) or (len(isbn) != 10)):
        print("Introduzca un ISBN correcto a validar: ")
        isbn = input()

    longitud = len(isbn)
    suma = 0
    for i in range(longitud):
        caracter = isbn[i]
        numero = int(caracter)
        suma = suma + (numero * (i+1))

    if(suma%11 == 0):
        print("El numero es correcto")
    else:
        print("ISBN INCORRECTO")

def validarMail():
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    check5 = False
    check6 = False
    repeticion = 0
    indiceArroba = 0

    print("Introduzca su email: ")
    email = input()

    longitud = len(email)

    #COMPROBACIONES

    if (email.find("@") != -1):
        check1 = True

    if(email.find(".") != -1):
        check2 = True

    if(email.startswith("@") == False and email.startswith(".") == False):
        check3 = True

    if(email.count("@") <=1):
        check4 = True

 
    if(email.find("@") < email.rfind(".")): #Buscamos el indice del ULTIMO punto
        check5 = True


    ultimoPunto = email.rfind(".")

    dominio = email[ultimoPunto + 1:]
    longitudDominio = len(dominio)
    if(longitudDominio >= 2 and longitudDominio <= 4):
        check6 = True

    #MENSAJES
    if(check1 == False):
        print("Falta un arroba")
    elif(check2 == False):
        print("Falta un punto")
    elif(check3 == False):
        print("No debe empezar por @ ni por punto")
    elif(check4 == False):
        print("Solo debe de haber un @")
    elif(check5 == False):
        print("Debe haber un punto despues de @")
    elif(check6 == False):
        print("El dominio debe tener de 2 a 4 caracteres")
    else:
        print("Bienvenido")

def mostrarLetra():
    print("Inserte un DNI: ")
    dni = input()

    if(dni.isdigit() and len(dni) == 8):
        dni = int(dni)
        letra = (dni - (math.trunc(dni/23)*23))

        cadenaSolucion = "TRWAGMYFPDXBNJZSQVHLCKET"

        print("Su letra del DNI es: " + cadenaSolucion[letra])
    else:
        print("DNI incorrecto")