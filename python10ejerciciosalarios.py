#variables
horas = 0
precioHora = 0
km = 0
horasBase = 36
horasExtra = 0
salarioExtra = 0
salario = 0
salarioTotal = 0

#PEDIR DATOS

print("Introduzca el numero de horas: ")
horas = int(input())
print("Introduzca el precio de la hora: ")
precioHora = int(input())
print("Introduzca los kilometros")
km = int(input())

if (km <= 100):
    print("DIETAS LOCALES")
elif (km >= 101 and km <= 500):
    print("DIETAS INTERNACIONALES")
else: 
    print("DIETAS INTERNACIONALES")

#SALARIO
if(horas < 36):
    salarioTotal = horas * precioHora
else:
    salario = horasBase * precioHora
    horasExtra = horas - horasBase
    salarioExtra = horasExtra * (precioHora + 2)
    salarioTotal = salarioExtra + salario

if (salarioTotal <= 250):
    print("NO TIENE RETENCION")
elif(salarioTotal >= 251 and salarioTotal <= 800):
    print("RETENCION 20%")
else:
    print("RETENCION 40%")

print("HORAS TRABAJADAS: "+ str(horas))
print("PRECIO HORA: "+ str(precioHora))
print("KILOMETROS: "+ str(km))
print("HORAS EXTRA: "+ str(horasExtra))
print("SALARIO BASE: "+ str(salario))
print("SALARIO EXTRA: "+ str(salarioExtra))
print("SALARIO FINAL: "+ str(salarioTotal))
