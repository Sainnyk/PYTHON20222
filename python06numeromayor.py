#PEDIR DOS NUMEROS AL USUARIO Y MOSTRAR EL NUMERO MAYOR DE LOS DOS

#Pedir datos
print("Introduzca un numero: ")
numero1 = int(input())

print("Introduzca otro numero: ")
numero2 = int(input())

if (numero1 > numero2):
    print("El numero mayor es: "+ str(numero1))
elif (numero2 > numero1):
    print("El numero mayor es: "+ str(numero2))
else:
    print("Los dos son iguales")