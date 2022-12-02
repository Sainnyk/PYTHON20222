#DEBEMOS MOSTRAR *UN* MENSAJE CON EL ERROR (SI LO TIENE)
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


# for i in range (longitud):
#     if(email[i] == "@"):
#         repeticion += 1
#         if(repeticion > 1):
#             check4 = False
#     if (repeticion == 0):
#         check4 = True
#OPCION SIN BUCLES:
if(email.count("@") <=1):
    check4 = True

# for i in range (longitud):
#     if(email[i] == "@"):
#         indiceArroba = i
#     for k in range(indiceArroba,longitud):
#         if(email[k] == "."):
#             check5 = True
#OPCION SIN BUCLES:  paco@gmaiil.com -> @ = 5   . = 2 (el punto iria por delante)
if(email.find("@") < email.rfind(".")): #Buscamos el indice del ULTIMO punto
    check5 = True

# dominio = email[indiceArroba+1:]
# longitudDominio = len(dominio)


# if(longitudDominio >= 2 and longitudDominio <= 4):
#     check6 = True
#OPCION PACO SIN WEAS:
ultimoPunto = email.rfind(".")
#CORTAMOS LA CADENA DESDE EL ULTIMO PUNTO EN ADELANTE (el dominio es a partir del .)
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