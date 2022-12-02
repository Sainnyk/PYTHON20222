#PEDIR NUMEROS HASTA QUE NO QUERAMOS CONTINUAR

texto = "s"

while(texto == "s"):
    print("Introduzca un numero: ")
    numero = int(input())

    if(numero > 0):
        print("POSITIVO")
    elif(numero < 0):
        print("NEGATIVO")
    else:
        print("ZERO")

    print("¿Desea continuar? (s/n)")
    texto=input()