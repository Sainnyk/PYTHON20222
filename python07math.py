#LIBRERIAS

#SINTAXIS CON FROM
from math import floor, ceil, trunc

numero1 = 20
numero2 = 3

division = numero1 / numero2
print("La division es " + str(division))

#METODOS DE LA LIBRERIA
varFloor = floor(division)
varCeil = ceil(division)
varTrunc = floor(division)
print("El numero redondeado hacia abajo es: " + str(varFloor))
print("El numero redondeado hacia arriba es: " + str(varCeil))
print("El numero truncado es: " + str(varTrunc))