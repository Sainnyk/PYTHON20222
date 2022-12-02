import math

print("Inserte un DNI: ")
dni = input()

if(dni.isdigit() and len(dni) == 8):
    dni = int(dni)
    letra = (dni - (math.trunc(dni/23)*23))

    cadenaSolucion = "TRWAGMYFPDXBNJZSQVHLCKET"

    print("Su letra del DNI es: " + cadenaSolucion[letra])
else:
    print("DNI incorrecto")