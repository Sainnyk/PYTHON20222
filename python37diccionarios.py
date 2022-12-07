import json

print("EJEMPLO DICCIONARIOS EN PYTHON")

#La variable "data" es un diccionario JSON
data = {

    'employees' : [
        {

            'name' : 'John Doe',

            'department' : 'Marketing',

            'place' : 'Remote'
        },
        {
            'name' : 'Jane Doe',

            'department' : 'Software Engineering',

            'place' : 'Remote'
        },
        {
            'name' : 'Don Joe',

            'department' : 'Software Engineering',

            'place' : 'Office'
        }
    ]
}

#SI DESEAMOS REALIZAR UN PRINT DE UN DICCIONARIO, DEBEMOS CONVERTIRLO A STRING, USANDO "dumps()"
jsonString = json.dumps(data)
print(jsonString)

#SI DESEAMOS RECORRER O RECUPERAR ELEMENTOS DENTRO DEL DICCIONARIO DEBEMOS RECORRER data, YA QUE ES COMO UNA LISTA/COLECCION
#HAY QUE DECIR QUÉ QUIERES RECUPERAR (SU KEY), EN ESTE CASO SOLO TENEMOS employees
for elemento in data['employees']:
    print(elemento["name"])