


print("Introduzca un numero a sumar sus cifras: ")
aux = input()

while(aux.isdigit() == False):
    print("Introduzca solo numeros: ")
    aux = input()

#Si ha puesto solo numeros llegara a esta linea
#Debemos recorrer la longitud de caracteres del texto
longitud = len(aux)
#Declaramos una variable suma fuera del bucle, ya que necesitamos ir incrementando su valor dentro del mismo
suma = 0

for i in range(longitud):
    #Vamos a capturar cada caracter y luego convertilo a numero.
    #Declaramos dichas variables dentro del bucle porque solamente las vamos a utilizar ahi.
    #Recuperamos cada posicion de cada letra
    caracter = aux[i]
    #Convertimos cada caracter a numero
    numero = int(caracter)
    suma += numero

print("La suma de " + aux + " es " + str(suma))