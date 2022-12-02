
#VALIDACION ISBN
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