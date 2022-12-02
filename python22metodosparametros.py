#---------METODOS CON PARAMETROS---------

def saludo(nombre):
    print("Bienvenido " + nombre)

def despedida(nombre, dia):
    print("Ha sido un placer hoy "+ dia + ", " + nombre)

#PROGRAMA PRINCIPAL

print("¿Cómo se llama?")
nombre=input()
print("¿Qué dia es hoy?")
day=input()

nombre= nombre.upper()
saludo(nombre)
despedida(nombre,day)