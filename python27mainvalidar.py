from python27funcionalidadmetodos import *

seleccion = 1
while(seleccion != 4):
    menu()
    seleccion = int(input())

    if(seleccion == 1):
        validarMail()
    elif(seleccion == 2):
        validarIsbn()
    elif(seleccion == 3):
        mostrarLetra()
    elif(seleccion == 4):
        print("¡Hasta luego!")
    