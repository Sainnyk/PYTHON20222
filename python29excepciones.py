def mostrarDoble():
    try:
        print("Introduzca un numero: ")
        numero = int(input())
        doble = numero * 2
        print("El doble del numero es "+ str(doble))
    except:
        print("Error, debe introducir un numero")
        mostrarDoble()

def dividirNumeros():
    try:
        print("Introduzca un numero: ")
        numero1 = int(input())
        print("Introduzca otro numero: ")
        numero2 = int(input())

        division = numero1 / numero2
    # except ValueError:
    #     print("Error, solamente numeros")
    # except ZeroDivisionError:
    #     print("No se puede dividir entre 0")
    except:
        print("Error general") #Cuando no sabemos que otros error pueden salir. Tambien se puede poner solo este directamente
    finally:
        print("Siempre me ejecuto, con o sin excepcion")
#----------- PROGRAMA PRINCIPAL---------------

print("Programa principal de control de excepciones")
dividirNumeros()

#Como buena praxis, debemos cerrar las conexiones, en este caso cerrar la base de datos. Lo hariamos en finally
try:
    print("Conectando a BBDD")
    print("Leyendo registros")
except:
    print("Error en acceso a datos")
finally:
    print("Cerrando conexion BBDD")
# try:
#     mostrarDoble()
# except ValueError:
#     print("Error, debe introducir un numero")
#     mostrarDoble() #este daria error, para arreglarlo habria que meter el try except dentro del metodo