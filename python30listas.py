


#DECLARAMOS UNA VARIABLE CON VARIOS NOMNRES
#LA VAMOS A USAR EN EL MAIN Y EN LOS METODOS
nombres = ["Huevito","Girasolito", "Cerdita","Peppa Pig"]

def mostrarNombres():
    #Dibujamos los nombres con un bucle de Referencia
    #for name in nombres:
    #   print(name)
    #Lo hacemos con un bucle contador porque quiero visualizar las posiciones de cada nombre
    for i in range(len(nombres)):
        name = nombres[i]
        print(str(i)+ ".-"+name)


print("Ejemplo de listas Python")
# #AÑADIMOS UN NUEVO NOMBRE
# nombres.append("El nuevo")
# #INSERTAMOS UN ELEMENTO EN EL MEDIO
# nombres.insert(1,"El de en medio")
# #ELIMINAMOS USANDO REMOVE
# nombres.remove("Cerdita")
# #ELIMINAMOS USANDO INDICE
# nombres.pop(6)
# mostrarNombres()
print("Listas de numero enteros")
numeros=[20,4,15,35,434,23,52,12]
#Orden ascendente
numeros.sort()
#Orden descendente
#numeros.sort(reverse = True)

for num in numeros:
    print(num)