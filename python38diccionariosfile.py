import json

print("Leer documento JSON con diccionarios")

file = open("jugadores_nokey.json", "r")

#Para transformar los datos json en formato diccionario se usa el metodo load()
data = json.load(file)
for jugador in data:
    print(jugador["nombre"])

file.close()

#SI DESEAMOS AÑADIR NUEVOS ELEMENTOS A NUESTRO DICCIONARIO HAY QUE CREAR UN NUEVO OBJETO (UN NUEVO {})
# {'numero': 1, 'nombre': 'Keylor Navas', 'posicion': 'Portero', 'edad': 28, 'imagen': 'https://patata.com'}
#{'clave' : valor, 'clave': valor}
#SE USA EL METODO APPEND (QUE LO AÑADE AL FINAL)
#UN OBJETO DICCIONARIO SE CREA MEDIANTE LLAVES, COMO SE HA DICHO EN LA LINEA 14

newPlayer = {
    "numero": 99,
    "nombre": "Error Garcia",
    "posicion": "Defensa de nada",
    "edad": 21,
    "imagen": ""
}

#AÑADIMOS A LA COLECCION DE DICCIONARIO UN NUEVO ELEMENTO
data.append(newPlayer)

#UNA VEZ QUE TENEMOS LOS DATOS EN data DEBEMOS VOLVER A ESCRIBILOS EN EL ARCHIVO (EN FORMATO JSON STRING), ES DECIR,
#DEBEMOS CONVERTIR LA COLECCION DICCIONARIO EN STRING USANDO dumps (EL METODO dumps DICE: CONVERTIR DICCIONARIO A STRING)
jsonString = json.dumps(data)

#ABRIMOS EL FICHERO DE NUEVO, PERO EN MODO ESCRITURA
file = open("jugadores_nokey.json", "w+")
file.write(jsonString)
file.flush()
file.close()