#MULTIPLICACION

#resultado= 0 Como solo la quiero en el bucle no la inicio aqui

print("Inserte un numero: ")
numero = int(input())

for i in range(11): 
    resultado = numero * i
    print(str(numero) + " * " + str(i) + " = " + str(resultado))