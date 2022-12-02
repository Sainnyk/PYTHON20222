#Todo numero 1 sera entero siguiendo una serie de pasos

print("Inserte un numero: ")
numero = int(input())

while(numero != 1):
    if(numero%2 == 0): #Si el numero es par
        numero = numero / 2
    else:
        numero = (numero * 3) +1

    print(int(numero))